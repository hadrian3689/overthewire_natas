import requests
import re

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    flag = re.findall("password for natas2 is(.*)-->",site.text)
    print("The flag for natas1 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas1.natas.labs.overthewire.org/"
    username = "natas1"
    password = "g9D9cREhslqBKtcA2uocGHPfMZVzeFK6"
    flag(url,username,password)
