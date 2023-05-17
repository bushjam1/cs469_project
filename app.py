from flask import Flask, request, jsonify
from urllib.parse import urlparse
import json 

from img_to_text import request_img, preprocess, ocr_img

import requests

import os 

app = Flask(__name__)

def validate_url(url):
    """Take url, return True if valid url and contains image, False otherwise. 
    
    Keyword arguments: 
    url -- requies scheme, netloc, and supported image extension to be valid
    """
    result = urlparse(url)
    supported_image = url.split('.')[-1] in ['jpg', 'png']
    print("scheme:", result.scheme)
    print("netloc:", result.netloc)
    print("is image:", supported_image)
    return all([result.scheme, result.netloc, supported_image])

def get_img_text(url):
    print("Requesting...")
    img = request_img(url)
    print("Request successful.")
    preprocessed = preprocess(img)
    print("Preprocess successful.")
    text = ocr_img(preprocessed)
    print("OCR successful.")
    print(text)


@app.route('/api', methods=["GET"])
def api():

    response = None
    url = ''

    # check if passed url 
    url = request.args['url']

    # validate passed url 
    if not validate_url(url):
        response = "error: url invalid"
    else: 
        response = get_img_text(url)

    

    return jsonify({'response': response})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='localhost.',port=port, debug=True)