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

# Mengimpor fungsi-fungsi yang sudah dibuat dengan penuh jerih payah
from src.f01 import *
from src.f02 import *
from src.f15 import *
from src.f16 import *
from global_var import *

# print("Mohon maximize window command prompt Anda untuk pengalaman terbaik.")
# time.sleep(3)
# for i in range(5):
#     remove_nth_line(1)
#     print(f"Memulai program dalam {5-i} detik...")
#     time.sleep(1)
# remove_nth_line(1)
# print("Selesai!")
# time.sleep(2)
# remove_nth_line(1)
# remove_nth_line(1)

while True:
    action = input()
    remove_nth_line(1)
    match lower(action):
        case "login":
            login()
            print("Berhasil login!")
        case "register":
            register()
            print("Berhasil register!")
        case "save":
            save(user_db, "data/user.csv")
            print("Berhasil menyimpan!")
        case "exit":
            exit()
            break
        case _:
            continue
