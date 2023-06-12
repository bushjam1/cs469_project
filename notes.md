# OCR
https://medium.com/nanonets/a-comprehensive-guide-to-ocr-with-tesseract-opencv-and-py>


# Speed up tesseract
https://github.com/tesseract-ocr/tessdata_fast
https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc
https://github.com/madmaze/pytesseract

# Server

## Run the app 
gunicorn wsgi:app 
flask run config in __main__
based on https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04


## UFW
configured access to port 5000 with this rule
`sudo ufw allow from 10.0.0.3 to any port 5000`
https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands


## Access and Error Logs
/var/log/nginx/access.log
/var/log/nginx/error.log

## Linode Guide on Flask + Nginx + Gunicorn + Ubuntu
https://www.linode.com/docs/guides/flask-and-gunicorn-on-ubuntu/


## Flask Nginx configuration
https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/
