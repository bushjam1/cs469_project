import requests
import json 

def query_api(url):
    response = requests.get(f"http://10.0.0.1:5000/api?url={url}")
    text = json.loads(response.text)['response']
    print("\nDETECTED TEXT")
    print("="*30)
    print(text)

if __name__ == "__main__":
    url = input("Please enter a url to an image (.jpg or .png):\n")
    query_api(url)