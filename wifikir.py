#modüller
import os
import sys
import time


banner = """

WIFI PASSWORD SHOWER V1.0
CODED BY XALE ~ GitHub: @xaletr

"""

if sys.argv[1] in ['-w', '--wifi']:
 wifi = sys.argv[2]
 print(banner)
 print(" ")
 print(" ")
 time.sleep(3)
 os.system('netsh wlan show profiles "'+wifi+'" key=clear')
 print(" ")
 print(" ")
 print(" ")
 print("Şifre Key Content Bölümünde")

elif sys.argv[1] in ['--networks', '-n']:
 print(" ")
 print(" ")
 os.system('netsh wlan show profiles')
 print(" ")
 print(" ")
 print(" ")
