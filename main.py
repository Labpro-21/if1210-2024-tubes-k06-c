"""
TUGAS BESAR IF1210 DASAR PEMROGRAMAN
K06-C

19623116    Zulfaqqar Nayaka Athadiansyah	
19623296    Muhammad Ra'if Alkautsar
19623076    Daniel A. M. Sipayung
16523106    Naufal Fakhri Fadhlurrahman
16523146    Sacca Kovida Kasmaji

SEKOLAH TEKNIK ELEKTRO DAN INFORMATIKA
INSTITUT TEKNOLOGI BANDUNG
2024
"""

# Mengimpor library yang dibutuhkan
import os, sys, math, time, argparse, datetime
from src.f01 import *
from src.f02 import *
from src.f03 import *
# from src.f04 import *
# from src.f07 import *
# from src.f08 import *
from src.f09 import *
from src.f10 import *
from src.f10 import *
from src.f10 import *

print("Mohon maximize window command prompt Anda untuk pengalaman terbaik.")
time.sleep(3)
for i in range(5):
    remove_nth_line(1)
    print(f"Memulai program dalam {5-i} detik...")
    time.sleep(1)
remove_nth_line(1)
print("Selesai!")
time.sleep(2)
remove_nth_line(1)

mainInput=input(">>> ")
if mainInput.lower() =="register":
    register()
elif mainInput.lower()=="login":
    login()
elif mainInput.lower()=="logout":
    logout()
# elif mainInput.lower()=="help":
#     help()
# elif mainInput.lower()=="inventory":
#     getMonster(2)
# elif mainInput.lower()=="battle":
#     battle()
# elif mainInput.lower()=="arena":
#
# elif mainInput.lower()=="shop":
    # if 
    # else:
# elif mainInput.lower()=="laboratory":
# elif mainInput.lower()=="monster":
# elif mainInput.lower()=="load":
# elif mainInput.lower()=="save":
# elif mainInput.lower()=="exit":


    






























# # Mengimpor fungsi-fungsi yang sudah dibuat dengan penuh jerih payah
# src_path = os.path.join(os.path.dirname(__file__), 'src')
# data_path = os.path.join(os.path.dirname(__file__), 'data')
# sys.path.append(src_path)
# sys.path.append(data_path)

# from x01 import *
# from f14 import *
