import requests
import json 

def runtest(test_num, img_url, val):
    
    base_url = 'http://10.0.0.1:5000/api?url='
    url = base_url + img_url 
    # call the API with image URL, get response or error
    print("\n")
    print("="*80)
    print(f"Test number: {test_num}")
    response = requests.get(url)
    text =  json.loads(response.text)['response']
    print("URL",url)
    print("Status:",response.status_code)
    #print("Result:", text)
    if response.status_code == 200 and val in text.lower():
        print(f"FOUND {val}")
        print("TEST PASSED")

        return True
    else:
        print("TEST FAILED")
        print(f"Did not find: {val}")
        return False
    
def tests():

    img_urls = {
            'alexanderplatz':'https://live.staticflickr.com/3912/15349926286_992542ec2e.jpg',
            'account':'https://i.pinimg.com/736x/7b/08/c9/7b08c9eff1bce30f6e13afba65002f10.jpg',                   
            'turmstrasse':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/U-Bahn_Turmstra%C3%9Fe%2C_Berlin.jpg/320px-U-Bahn_Turmstra%C3%9Fe%2C_Berlin.jpg',
            'stop':'http://upload.wikimedia.org/wikipedia/commons/f/f9/STOP_sign.jpg'
            
            }

    results = {'pass':0,'fail':0}
    # test 1
    test_seq = 0 
    for key, val in img_urls.items():
        test_seq += 1
        res = runtest(test_seq, val, key)
        if res is True:
            results['pass'] += 1
        else:
            results['fail'] += 1
    print()
    print("="*80)
    print(f"RESULTS: tests passed: {results['pass']} tests failed: {results['fail']}")
    print()

if __name__ == "__main__":
    tests()
