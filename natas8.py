import requests
import re
import base64

def flag(url,username,password,hex_string):
    hex_decode = bytes.fromhex(hex_string).decode('utf-8')
    reverse = hex_decode[::-1]
    base64_string = reverse
    base64_bytes = base64_string.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes)
    secret = string_bytes.decode("ascii")
    post_data = {
            "secret":secret,
            "submit":"Submit+Query"
            }
    get_flag = requests.post(url,auth=(username,password),data=post_data)
    flag = re.findall("password for natas9 is(.*)",get_flag.text)
    print("The flag for natas8 is: " + flag[0].strip())

def login(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    get_source = re.findall('ref="(.*)">View',site.text)
    source_url = requests.get(url + get_source[0],auth=(username,password))
    hex_get = re.findall('<span style="color: #DD0000">"(.*)"',source_url.text)
    hex_string = hex_get[0][0:32]
    flag(url,username,password,hex_string)

if __name__=="__main__":
    url = "http://natas8.natas.labs.overthewire.org/"
    username = "natas8"
    password = "a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB"
    login(url,username,password)