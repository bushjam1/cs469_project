import requests

def runtest(test_num, url):
    
    base_url = 'http://10.0.0.1:5000/api?url='
    url = base_url + img_url 

    # call the API with image URL, get response or error
    print()
    print("="*80)
    print(f"Test number: {test_num}")
    response = requests.get(url)
    print("Status:",response.status_code)
    print("Result:",response.text)
    if response.status_code == 200:
        print("TEST PASSED")
    else:
        print("TEST FAILED", response.status_code, response.json)


def tests():

    img_urls = [

            ]
    # test 1
    img_url = 'https://i.pinimg.com/originals/42/84/0f/42840fafe6b8c8024c3cf7b6a7661957.jpg'
    runtest(1, img_url)

    # test 2 
    # test 3 
    # test 4
    # test 5


if __name__ == "__main__":
    tests()
