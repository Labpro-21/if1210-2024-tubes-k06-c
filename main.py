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
from nt import error
import os, argparse

# Mengimpor fungsi-fungsi yang sudah dibuat dengan penuh jerih payah
from src.x01 import *
from src.F01_Register import *
from src.F02_Login import *
from src.F15_Save import *
from src.F16_Exit import *

# argparse
parser = argparse.ArgumentParser(description="Menjalankan program dan memuat database csv")
parser.add_argument("dir", help="Direktori penyimpanan database CSV", nargs='?')
args = parser.parse_args()

if args.dir is None:
    os.system('cls')
    print("Tidak ada nama folder yang diberikan!")
    print("Penggunaan: python main.py <nama_folder>")
    sys.exit(1)
else:
    os.system('cls')
    csv_dir = str(args.dir)
    while not validate_dir("data/" + csv_dir):
        if validate_dir("data/" + csv_dir):
            load_data(csv_dir)
        else:
            print(f"Folder {csv_dir} tidak ditemukan! Mohon masukkan nama folder yang valid dalam direktori 'data'.")
            sys.exit(1)


# Loading Screen
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
remove_nth_line(1)

# Title Screen
print("data/title_screen.txt")

# Input Prompt
while True:
    action = input(">>> ")
    remove_nth_line(1)
    match lower(action):
        case "login":
            if logged_in:
                os.system('cls')
                print("Anda sudah login!")
            else:
                login(user_db)
                os.system('cls')
                logged_in = True

                print("Berhasil login!")
        case "register":
            os.system('cls')
            register(user_db)
            print("Berhasil register!")
        case "save":
            os.system('cls')
            print('data' + csv_dir + 'user.csv')
            save(user_db, 'data/' + csv_dir + '/user.csv')
            print("Berhasil menyimpan!")
        case "exit":
            os.system('cls')
            exit(csv_dir)
            break
        case _:
            continue