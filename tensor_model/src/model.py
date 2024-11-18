import tensorflow as tf
import numpy as np
from selenium import webdriver

# Path relative to api.py
model = tf.keras.models.load_model("../tensor_model/model.h5")  # From api.py
model.compile()


def predict_productivity(image_path: str) -> bool:
    img = tf.keras.utils.load_img(image_path, target_size=(128, 128))
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    return bool(prediction[0][0] > 0.5)


def take_screenshot(url: str):
    driver = webdriver.Chrome()
    driver.get(url)
    # Path relative to api.py
    driver.save_screenshot(
        "../tensor_model/dataset/real_time/"
        + url.replace("/", "$").replace(":", "#")
        + ".png"
    )
    driver.quit()
