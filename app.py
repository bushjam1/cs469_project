from flask import Flask, request, jsonify, render_template
from urllib.parse import urlparse
from urllib.parse import unquote
import json

from img_to_text import request_img, preprocess, ocr_img

import requests

import os

app = Flask(__name__)

with open("/etc/config.json") as config_file:
    config = json.load(config_file)

app.config["SECRET_KEY"] = config.get("SECRET_KEY")


def validate_url(url):
    """Take url, return True if valid url and contains image, False otherwise.

    Keyword arguments:
    url -- requies scheme, netloc, and supported image extension to be valid
    """
    result = urlparse(url)
    supported_image = url.split(".")[-1] in ["jpg", "png"]
    print(f"validate_url() \n scheme: {result.scheme} \n netloc: {result.netloc} \n is image: {supported_image}")
    return all([result.scheme, result.netloc, supported_image])


def get_img_text(url):
    print("Requesting...")
    img = request_img(url)
    if img is None:
        return "error: requested resource not available"
    print("Request successful.")
    preprocessed = preprocess(img)
    print("Preprocess successful.")
    text = ocr_img(preprocessed)
    print("OCR successful.")
    print(text)
    return text


@app.route("/cs469/api", methods=["GET"])
def api():
    response = None
    url = ""

    # get headers 
    print(request.headers)

    # check if passed url
    url = request.args["url"]

    # validate passed url
    if not validate_url(url):
        response = "error: url invalid"
    else:
        response = get_img_text(url)

    # return response in json
    return jsonify({"response": response})


@app.route("/cs469/gui", methods=["GET"])
def gui():
    response = None
    url = ""

    # check if passed url
    # url = request.args['url']

    # check headers
    print(request.headers)

    if request.method == "GET" and len(request.args) == 0:
        return render_template("gui.j2")

    else:
        url = unquote(request.args["url"])
        print("**URL", url)

        # validate passed url
        if not validate_url(url):
            response = "error: url invalid"
        else:
            response = get_img_text(url)

        # return response in text

        # return jsonify({'response': response})
        return render_template("response.j2", response=response)


if __name__ == "__main__":
    # former configuration
    # host = '10.0.0.1' #'localhost.'
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host=host, port=port, debug=True)
    # new config based on https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
    app.run(host="0.0.0.0")
