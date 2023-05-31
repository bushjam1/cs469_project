import requests

def runtest(test_num, url):
    
    base_url = 'http://10.0.0.1:5000/api?url='
    url = base_url + img_url 

    # call the API with image URL, get response or error
    print("\n","="*80)
    print(f"Test number: {test_num}")
    response = requests.get(url)
    print("Status:",response.status_code)
    print("Result:",response.json['response'])
    if response.status_code == 200:
        print("TEST PASSED")
    else:
        print("TEST FAILED", response.status_code, response.json)


def tests():

    img_urls = [    'https://live.staticflickr.com/3760/13307397783_5266496226_b.jpg',
                    'https://live.staticflickr.com/2397/2476584907_73def16be0.jpg',
                    'https://live.staticflickr.com/5342/13965039173_9fdb82e940_b.jpg'
                ]
    # test 1
    for i in range(len(img_urls)):
        runtest(i, img_url[i])

    # test 2 
    # test 3 
    # test 4
    # test 5


if __name__ == "__main__":
    tests()
