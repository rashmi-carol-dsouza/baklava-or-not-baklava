from flask import Flask, request, jsonify
from flask_api import status
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np

import logging

app = Flask(__name__)

class ImageNotProvided(Exception):
    """Raised when an image is not provided in the request"""
    pass


def pretrained_model(file_storage_img):

    # Loading the model
    model = load_model('../bvnb_model.h5')

    # Image processing
    img = Image.open(file_storage_img)
    img = img.resize((224, 224))
    X = image.img_to_array(img)
    X = np.expand_dims(X, axis = 0)
    images = np.vstack([X])

    # Model prediction
    val = model.predict(images)    
    return True if val == 0 else False


@app.post("/photo")
def upload_photo():
    try:
        img = request.files.get('image')
        if img == None:
            raise ImageNotProvided("Image not sent")
        response = { "is_baklava": pretrained_model(img) }
        return jsonify(response)
    except Exception as error:
        logging.exception(error)
        error_response = { "error": str(error) }
        return jsonify(error_response), status.HTTP_400_BAD_REQUEST