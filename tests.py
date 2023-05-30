import requests

def runtest(url):
    response = requests.get(url)
    print("Status:",response.status)
    print("Result:",response.json)
    if response.status_code == 200:
        print("TEST PASSED")
    else:
        print("TEST FAILED", response.status_code, response.json)


def tests():
    base_url = 'http://localhost:5000/api?url='

    # test 1
    print("Test 1")
    img_url = 'https://i.pinimg.com/originals/42/84/0f/42840fafe6b8c8024c3cf7b6a7661957.jpg'
    url = base_url + img_url
    runtest(url)



if __name__ == "__main__":
    tests()