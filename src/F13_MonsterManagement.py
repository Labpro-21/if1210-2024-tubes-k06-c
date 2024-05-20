"""
F13 - Monster Management
19623076 Daniel
19723296 Muhammad Ra'if Alkautsar
"""

# Kode di sini
# Memuat file .csv yang diperlukan

from src.F05_Monster import *
import sys, os
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(parent_path, 'data')
sys.path.append(parent_path)
sys.path.append(data_path)
from global_var import *
from src.x01 import *

def show_monster_database(monster_db):
    print(f"ID  | Type                | ATK Power    | DEF Power     | HP      |")
    for i in range(len(monster_db["type"])):
        print(f"{monster_db["id"][i]} | {monster_db["type"][atk_power]} | {monster_db["atk_power"][i]} | {monster_db["def_power"][i]} | {monster_db["hp"][i]}")

def add_monster(monster_db):
    monster_type = ""
    while True:
        monster_type = str(input("Masukkan tipe/nama monster: "))
        if is_numerical(monster_type):
            print("Input tidak valid!")
        if monster_type in monster_db["type"]:
            print("Monster sudah ada dalam database!")
        else:
            break
    while True:
        monster_atk = str(input("Masukkan ATK Power monster: "))
        if not is_numerical(monster_atk):
            print("Input tidak valid!")
        else:
            break
    while True:
        monster_def = str(input("Masukkan DEF Power monster: "))
        if not is_numerical(monster_def):
            print("Input tidak valid!")
        else:
            break
    while True:
        monster_hp = str(input("Masukkan HP monster: "))
        if not is_numerical(monster_hp):
            print("Input tidak valid!")
        else:
            break        
    monster_db["id"].append(len(monster_db["id"]) + 1)
    monster_db["type"].append(str(monster_type))
    monster_db["atk_power"].append(int(monster_atk))
    monster_db["def_power"].append(int(monster_def))
    monster_db["hp"].append(int(monster_hp))
    print("Monster berhasil ditambahkan.")

def remove_monster(monster_db):
    show_monster_database(monster_db)
    while True: 
        choice = str(input("Masukkan ID monster yang ingin dihapus (ketik 'exit' untuk keluar): "))
        if choice == "exit":
            break
        elif is_numerical(choice) == False:
            print("Input harus berupa angka!")
        else: 
            if choice >= 1 and choice <= len(monster_db["type"]):
                monster_idx = int(input("Masukkan ID monster yang ingin dihapus: ") - 1)
                monster_db["id"] = remove_ele(monster_idx, monster_db["id"])
                monster_db["type"] = remove_ele(monster_idx, monster_db["type"])
                monster_db["atk_power"] = remove_ele(monster_idx, monster_db["atk_power"])
                monster_db["def_power"] = remove_ele(monster_idx, monster_db["def_power"])
                monster_db["hp"] = remove_ele(monster_idx, monster_db["hp"])
                print("Monster berhasil dihapus.")
            else:
                print("Monster tidak ditemukan.")
    return monster_db

def change_monster(monster_db):
    show_monster_database(monster_db)
    while True:
        choice = str(input("Masukkan ID monster yang ingin diubah (ketik 'exit' untuk keluar): "))
        if choice == "exit":
            break
        elif is_numerical(choice) == False:
            print("Input harus berupa angka!")
        else:
            choice = int(choice)
            if choice >= 1 and choice <= len(monster_db["type"]):
                monster_idx = int(input("Masukkan ID monster yang ingin diubah: ") - 1)
                monster_type = str(input("Masukkan tipe/nama monster: "))
                monster_atk = int(input("Masukkan ATK power monster: "))
                monster_def = int(input("Masukkan DEF power monster: "))
                monster_hp = int(input("Masukkan HP monster: "))
                monster_db["type"][monster_idx] = monster_type
                monster_db["atk_power"][monster_idx] = monster_atk
                monster_db["def_power"][monster_idx] = monster_def
                monster_db["hp"][monster_idx] = monster_hp
                print("Monster berhasil diubah.")
            else:
                print("Monster tidak ditemukan.")
    return monster_db

def monster_management(monster_db):
    while True:
        choice = str(input("Ketik 'tambah' untuk menambahkan monster, 'hapus' untuk menghapus monster, dan 'ubah' untuk mengubah monster.").lower())
        if is_numerical(choice):
            print("Input harus berupa teks!")
        else:
            if choice == "tambah":
                add_monster(monster_db)
            elif choice == "hapus":
                remove_monster(monster_db)
            elif choice == "ubah":
                change_monster(monster_db)
            else:
                print("Input tidak valid!")

# def monsterManagement():
#     print("""
# SELAMAT DATANG DI DATABASE PARA MONSTER !!!
# 1. Tampilkan semua Monster
# 2. Tambah Monster baru      
#       """)
#     pilihan = int(input(">>> Pilih aksi : "))
#     if pilihan == 1:
#         print("""
#  ID  | Type                | ATK Power    | DEF Power     | HP      |""")
#         for i in range (len(monster_db["type"])):
#                         print(f"""
#  {monster_db["id"][i]}  | {monster_db["type"][i]}                | {monster_db["atk_power"][i]}    | {monster_db["def_power"][i]}     | {monster_db["hp"][i]}      |""")
#     elif pilihan == 2:
#         addType = ''
#         addATKP = ''
#         addDEFP = ''
#         addHP = ''
#         print("Memulai pembuatan monster baru")
#         added = False
#         while added == False:
#             if addType == '':
#                 addType = input(">>> Masukkan Type / Nama : ")
#             elif addType not in monster_db["type"]:
#                   monster_db["id"].append(last(monster_db["id"])+1)
#                   monster_db["type"].append(addType)
#                   added = True
#             else:
#                 print("Nama sudah terdaftar, coba lagi")


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
