"""
F01 - Register
19623116 Nayaka & 19623076 Daniel
"""

import os, sys
# Membuka database yang sudah di-load dan disimpan di global_var
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(parent_path, 'data')
sys.path.append(parent_path)
sys.path.append(data_path)

# Memuat database yang sudah disimpan di dictionary `user_db` dalam module global_var

from test_db import * #ganti test_db -> global_var
from src.f02 import *

# FUNGSI register()
def register(user_db: dict) -> dict:
    # Ra'if ini ntar tolong dicakepin yah itunya
    print("<=============>")
    print("  O. W. C. A.  ")
    print("   We serve.   ")
    print("<=============>")

    # Bagian utama fungsi
    username = input_username_reg()
    if is_in(username, user_db["username"]):
            print(f"Username sudah ada, login dengan username '{username}' atau gunakan username lain !")
    else:
        password = input("Password: ")
        # Menambahkan data pengguna ke dalam database
        user_db["id"].append(last(user_db["id"]) + 1)
        user_db["username"].append(username)
        user_db["password"].append(password)
        user_db["role"].append('agent')
        user_db["oc"].append(0)
        
        save(user_db, 'data/' + 'user.csv')
        whoLogin(username)

        # Memilih monster pertama
        print()
        print("Silahkan pilih salah satu monster sebagai monster awalmu!")
        id_num = 0
        for i in monster_db["type"] :
            id_num+=1
            print(f"{id_num}. {i}")
        idSelectedMon = int(input("Monster pilihanmu : "))
        print(user_db["password"])
        print(monster_db["type"])
        agent = user_db["password"][0]
        monster = monster_db["type"][idSelectedMon-1]
        print(f"Selamat datang Agent {agent}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster}!")

    return user_db

# FUNGSI input_username_reg()
def input_username_reg():
    valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    username = input("Username: ")

    valid = subset(username, valid_char)
    while not valid:
        remove_nth_line(1)
        print("Username hanya boleh berisi alfabet, angka, tanda hubung bawah (_), dan tanda strip (-)!")
        username = input("Username: ")
        remove_nth_line(1)
        valid = subset(username, valid_char)
        if valid:
            remove_nth_line(1)
    return username

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
Fungsi register() akan mendaftarkan akun baru untuk agent dengan username dan password
sesuai dengan yang diinput oleh pengguna. Fungsi input_username_reg() digunakan untuk
menerima username dari akun yang akan dibuat dan memvalidasinya. 

Di sini global_var dimuat agar kita dapat mengakses database username dari user.csv yang sudah di-load.
Perhatikan bahwa remove_nth_line() yang merupakan fungsi dari x01 dapat digunakan tanpa
memuat x01.py secara eksplisit karena sudah dimuat lewat f14 dari global_var.
"""