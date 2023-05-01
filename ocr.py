import sys
import pytesseract
from PIL import Image
from io import BytesIO
import requests

from datetime import datetime

def request_img(url):
  """Return image from internets with Requests and passed url. 
  
  Keyword arguments:
  url -- url to image
  """
  response = requests.get(url)
  if response.status_code != 200:
    raise Exception("URL Error: check URL and try again")
  return response


def ocr_img(response):
  """Recognize text with Tesseract and return string. 

  Keyword arguments:
  response -- response from request_img
  """

  img = Image.open(BytesIO(response.content))
  config = "-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6" #oem: default OCR engine; psm: assume single block text
  # config = r'--oem 3 --psm 6' #oem: default OCR engine; psm: assume single block text
  text = pytesseract.image_to_string(img, config=config, lang="eng")
  return text

if __name__ == "__main__":
  if len(sys.argv) == 2:
    url = sys.argv[1]
  else:
    raise Exception("Usage: python3 py_ocr.py <image_url.jpg>")
    #url = "test.jpg"

  response = request_img(url)#sys.argv[1])
  start = datetime.now()
  text = ocr_img(response)
  print(text)
  print(f"time elapsed: {datetime.now() - start}")
