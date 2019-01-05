#/usr/bin/python
# Thanks To Aylward Hxr
# (c) Hax28dh8Sec
# modif by KANG-NEWBIE
import os
import subprocess as sp
os.system('clear')
print("[!] Please Wait...")
sp.call('pip install requests', shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)
import requests

os.system("clear")
print("""
\033[1;32m+---------------------------------------+
\033[1;32m|\033[1;31m          SPAM TELEPON MASAL           \033[1;32m|
\033[1;32m|\033[1;37m  CREATE BY WIDHISEC ft. KANG-NEWBIE   \033[1;32m|
\033[1;32m+---------------------------------------+
(*) Ketik Enter Untuk Melewati Step""")
no1 =input("Masukkan Nomor Telepon1 =>")
no2 =input("Masukkan Nomor Telepon2 =>")
no3 =input("Masukkan Nomor Telepon3 =>")
no4 =input("Masukkan Nomor Telepon4 =>")
no5 =input("Masukkan Nomor Telepon5 =>")
print("[-] STATUS:")
r1 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no1)
print("[+] SPAM1",r1.json()["msg"])
r2 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no2)
print("[+] SPAM2",r2.json()["msg"])
r3 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no3)
print("[+] SPAM3",r3.json()["msg"])
r4 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no4)
print("[+] SPAM4",r4.json()["msg"])
r5 = requests.get('https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor='+no5)
print("[+] SPAM5",r5.json()["msg"])
print("")
