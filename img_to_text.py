from PIL import Image
import sys
import requests
from io import BytesIO
import pytesseract
from datetime import datetime


# Obtian image 

def request_img(url):
  """Return image from internets with Requests and passed url. 
  
  Keyword arguments:
  url -- url to image
  """
  response = requests.get(url)
  if response.status_code != 200:
    raise Exception("URL Error: check URL and try again")
  img = Image.open(BytesIO(response.content))

  return img


# Preprocess image 

# grayscale 
def grayscale(img):
    return img.convert("L")

# edging
def edge(img):
    return img.filter(ImageFilter.FIND_EDGES)

# thresholding 
def threshold(img, thresh):
    return img.point(lambda x: 255 if x > thresh else 0)

# invert
def invert(img):
    return ImageOps.invert(img)

def preprocess(img):
    img_gray = grayscale(img)
    img_threshold = threshold(img_gray, 180)
    result = img_threshold
    return result 



def ocr_img(img):
  """Recognize text with Tesseract and return string. 

  Keyword arguments:
  response -- response from request_img
  """

#   img = Image.open(BytesIO(response.content))
  #config = "--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz" #oem: default OCR engine; psm: assume single block text
  config = r'--oem 3 --psm 6' #oem: default OCR engine; psm: assume single block text
  text = pytesseract.image_to_string(img, config=config, lang="eng")
  return text



if __name__ == "__main__":
  if len(sys.argv) == 2:
    url = sys.argv[1]
  else:
    # raise Exception("Usage: python3 py_ocr.py <image_url.jpg>")
    url = "https://i.pinimg.com/736x/7b/08/c9/7b08c9eff1bce30f6e13afba65002f10.jpg"

    print("Requesting...")
    img = request_img(url)
    print("Request successful.")
    preprocessed = preprocess(img)
    print("Preprocess successful.")
    text = ocr_img(preprocessed)
    print("OCR successful.")
    print(text)