import tensorflow as tf
import shutil
from fastapi import FastAPI, UploadFile, File
import numpy as np
import os

model = tf.keras.models.load_model(
    "model.h5"
)  # Replace with the path to your saved model

def predict_image(file: UploadFile = File(...)):
    # Save the uploaded file
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Predict productivity
    result = predict_productivity(file_location)

    # Clean up the temporary file
    os.remove(file_location)

    return {"productive": result}

# Takes uploaded image and returns if productuve or not
def predict_productivity(image_path: str) -> bool:

    # Load and preprocess the image
    img = tf.keras.utils.load_img(image_path, target_size=(128, 128))
    # load_img(image_path, target_size=(128, 128))
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict using the model
    prediction = model.predict(img_array)
    return bool(prediction[0][0] > 0.5)
