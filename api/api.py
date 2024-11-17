import sys
import os
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import shutil
import tensorflow as tf

import numpy as np


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db import add_website as db_add_website, get_productive_value


model = tf.keras.models.load_model("model.h5")  # Replace with the path to your saved model


class Website(BaseModel):
    url: str

#Takes uploaded image and returns if productuve or not
def predict_productivity(image_path: str) -> bool:

    # Load and preprocess the image
    img = tf.keras.utils.load_img(image_path, target_size=(128, 128))
    # load_img(image_path, target_size=(128, 128))
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict using the model
    prediction = model.predict(img_array)
    return bool(prediction[0][0] > 0.5)



def decide_productivity(url: str) -> bool:
    # TODO: Call ML model to predict productivity
    return True

def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1:5500"],  # Allow frontend URL
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allows all headers
    )
    

    @app.get("/")
    def read_root():
        return {"message": "Hello, World!"}

    @app.post("/add-website")
    def add_website(website: Website):
        productive = get_productive_value(website.url)
        if productive is None:
            productive = decide_productivity(website.url)
            db_add_website(website.url, productive)
        return {"url": website.url, "productive": productive}



    @app.post("/predict")
    async def predict_image(file: UploadFile = File(...)):
        # Save the uploaded file
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Predict productivity
        result = predict_productivity(file_location)

        # Clean up the temporary file
        os.remove(file_location)

        return {"productive": result}
    return app


    

app = create_app()


