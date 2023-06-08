# OCR
https://medium.com/nanonets/a-comprehensive-guide-to-ocr-with-tesseract-opencv-and-py>


# Speed up tesseract
https://github.com/tesseract-ocr/tessdata_fast
https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc
https://github.com/madmaze/pytesseract

# Server

## Run the app 
gunicorn wsgi:app 

## UFW
configured access to port 5000 with this rule
`sudo ufw allow from 10.0.0.3 to any port 5000`

## Access and Error Logs
/var/log/nginx/access.log
/var/log/nginx/error.log

## Linode Guide on Flask + Nginx + Gunicorn + Ubuntu
https://www.linode.com/docs/guides/flask-and-gunicorn-on-ubuntu/


## Flask Nginx configuration
https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/
