from flask import Flask, request, jsonify
from flask_api import status

import logging

app = Flask(__name__)

class ImageNotProvided(Exception):
    """Raised when an image is not provided in the request"""
    pass

# TODO: Delete this temporary mock function once the model function call is ready
def pretrained_model(image):
    import random
    return random.choice([True, False])

@app.post("/photo")
def upload_photo():
    try:
        img = request.files.get('image')
        if img == None:
            raise ImageNotProvided("Image not sent")
        # TODO: Replace the call below with the actual call to the model fn
        response = { "is_baklava": pretrained_model(img) }
        return jsonify(response)
    except Exception as error:
        logging.exception(error)
        error_response = { "error": str(error) }
        return jsonify(error_response), status.HTTP_400_BAD_REQUEST