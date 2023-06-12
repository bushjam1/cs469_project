# Intro 

Image-to-Text is a web-based application that allows users to submit URL to an image on the web in .jpg or .png format and receive back text extracted from the image. For example, a user might wish to extract text from a photo of a document (e.g., an example contract) online, so that they can paste the text into a word processing application. The target audience is casual users who wish to manually or programmatically extract text from web-based images. 

# Installation 

Use of the application optimally requires setting up VPS hosting and only supports Linux installation. A local instance can be run with minor configuration changes. 

To run the application on a VPS: 

1. Obtain a Linux VPS instance. 
2. Set up and secure the server (make sure to install UFW, as it is required to manage port access). 
3. Log into the server with sudo privileges.  
4. Install Nginx (https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/)
5. Install Tesseract (https://tesseract-ocr.github.io/tessdoc/Installation.html)
6. Install Pip (https://pip.pypa.io/en/stable/installation/) 
7. Make a project directory in the home folder of the VPS, e.g., /image-to-text. 
8. Clone this repo into the project directory. 
9. Create a virtual environment in the project directory with `python3 -m venv <env>`. 
10. Activate the virtual environment with `source <env>/bin/activate`. 
11. Install dependencies with the command `pip -m install -r requirements.txt` within the project directory. 
12. Configure Nginx HTTP server, the Flask application (app.py), and the WSGI server according to the Nginx, Flask, and Gunicorn documentation. (See https://flask.palletsprojects.com/en/2.1.x/deploying/gunicorn/; https://flask.palletsprojects.com/en/2.0.x/deploying/wsgi-standalone/.) 
13. Open port 80 with UFW. 
14. Run the application with `gunicorn -w 3 wsgi:app -D`. 
15. Kill the application with `pkill -u <username> gunicorn`. 

# Features and Functionality 

The application has two interfaces: a graphical user interface ("GUI") and a text-based application programming interface ("API").  

    - In the GUI, extracted text is displayed in easily readable font within a results box in an arrangement approximating that found in the original image. The GUI is mobile-friendly and includes additional user feedback, such as usage tips, a loading icon, and navigation links. 
      
    - In the API, users receive back a JSON response with all detected text, including newline characters "\n" so that the text can be properly displayed, once received. 

If either version of the application encounters an error, it will report the error to the user in the response. For example, an invalid URL will generate a error message to the user, "error: url invalid". 

# Usage Instructions: General 

The application works best with images containing machine-printed text that is clear, high-contrast, and flatly displayed. Black-and-white printed receipts or printed documents generally produce excellent results. Images with text that is is unclear, low-contrast, or non-orthogonal to the point of view can produce poor results. The presence of additional non-text imagery within the image can also create poor results. The application can, however, process good handwriting!

## Usage Instructions: GUI 

To access the GUI, use a web browser to navigate to the specified IP and port in your configuration, e.g. http://localhost:5000/gui. Note that HTTPS is not currently supported, so users should click through any warning in their browser to access the application. That said, don't submit anything sensitive! 

In the text submission box on the main page, enter a URL to an image on the web in .jpg or .png format and click "Submit". Depending on the size of the image, the results could take up to 10 seconds to return back. 

Click "Try another!" to navigate back to the main page. Errors are displayed in the same text box. 

## Usage Instructions: API 

To access the API, use the IP and port in your configuration, e.g. http://localhost:5000/gui. The API accepts GET requests with a single query parameter: url:<value>. The URL supplied must have the method (HTTP://), a domain (example.com), and an image specified in .jpg or .png format (/image1.jpg) to be valid. Note that text results will be contained within a JSON response with the following structure: {"results":"<text results>"}.

Another way to do it would to be to use a CLI request tool like curl. Another option exists in the code repository. There, a script is included called tests.py. After running pip install -r requirements.txt, in the project directory, running this script with python3 tests.py will query the API with 4 example images. The way tests are currently configured, "FAILED" means that the searched-for word was not located in the extracted text. Python will report errors for any other errors encountered. 