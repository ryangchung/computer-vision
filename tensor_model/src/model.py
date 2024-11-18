import tensorflow as tf
import numpy as np
from selenium import webdriver
import hashlib

# Path relative to api.py
model = tf.keras.models.load_model("../tensor_model/model.h5")  # From api.py
model.compile()


def predict_productivity(image_path: str) -> bool:
    img = tf.keras.utils.load_img(image_path, target_size=(128, 128))
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    return bool(prediction[0][0] < 0.5)


def take_screenshot(url: str) -> str:
    driver = webdriver.Chrome()
    driver.get(url)
    # Path relative to api.py
    hashed_url = hashlib.sha256(url.encode()).hexdigest()
    image_path = "../tensor_model/dataset/real_time/" + hashed_url + ".png"
    driver.save_screenshot(image_path)
    driver.quit()
    return image_path
