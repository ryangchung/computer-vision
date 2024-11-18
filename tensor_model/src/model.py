import tensorflow as tf
import numpy as np
from selenium import webdriver
from PIL import Image

model = tf.keras.models.load_model("../tensor_model/model.h5")  # From api.py
model.compile()


# Takes uploaded image and returns if productuve or not
def predict_productivity(image_path: str) -> bool:

    # Load and preprocess the image
    img = tf.keras.utils.load_img(image_path, target_size=(128, 128))
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict using the model
    prediction = model.predict(img_array)
    return bool(prediction[0][0] > 0.5)


def take_screenshot(url: str):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.save_screenshot(
        "../tensor_model/dataset/real_time/"
        + url.replace("/", "$").replace(":", "#")
        + ".png"
    )
    driver.quit()
