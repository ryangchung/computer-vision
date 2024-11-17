import tensorflow as tf
import numpy as np

import os


# Absolute path to model.sh5
model_path = os.path.join(os.path.dirname(__file__), '../src/model.h5')

# Load the model
model = tf.keras.models.load_model(model_path)



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

