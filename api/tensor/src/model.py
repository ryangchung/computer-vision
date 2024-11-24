import tensorflow as tf
import numpy as np
from selenium import webdriver
import hashlib

class ProductivityModel:
    def __init__(self, model_path: str):
        self.model = tf.keras.models.load_model(model_path)
        self.model.compile()

    def predict_productivity(self, image_path: str) -> bool:
        img = tf.keras.utils.load_img(image_path, target_size=(128, 128))
        img_array = tf.keras.utils.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = self.model.predict(img_array)
        return bool(prediction[0][0] < 0.5)

    def take_screenshot(self, url: str) -> str:
        driver = webdriver.Chrome()
        driver.get(url)
        hashed_url = hashlib.sha256(url.encode()).hexdigest()
        image_path = "tensor/dataset/prod/" + hashed_url + ".png"
        driver.save_screenshot(image_path)
        driver.quit()
        return image_path
