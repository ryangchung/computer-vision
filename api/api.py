import sys
import os
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import shutil




import numpy as np


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db import add_website as db_add_website, get_productive_value
from tensor_model.src.model import predict_productivity




class Website(BaseModel):
    url: str




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



    #To predict if productive
    @app.post("/predict")
    async def predict_image(file: UploadFile = File(...)):
        # Save the uploaded file
        file_location = f"temp_{file.filename}"
        print(f"Received file: {file.filename}")  # Debugging log
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Predict productivity
        result = predict_productivity(file_location)
        print(f"Prediction result: {result}")  # Debugging log

        # Clean up the temporary file
        os.remove(file_location)  # Uncomment to clean up temp file

        return {"productive": result}

    return app


    

app = create_app()


