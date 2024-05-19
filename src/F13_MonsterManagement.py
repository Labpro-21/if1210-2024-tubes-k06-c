"""
F13 - Monster Management
19623076 Daniel
"""

# Kode di sini
# Kode di sini
from F05_Monster import *
import sys, os
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(parent_path, 'data')
sys.path.append(parent_path)
sys.path.append(data_path)

# Memuat file .csv yang diperlukan
from global_var import *
from x01 import *

def monsterManagement():
    print("""
SELAMAT DATANG DI DATABASE PARA MONSTER !!!
1. Tampilkan semua Monster
2. Tambah Monster baru      
      """)
    pilihan = int(input(">>> Pilih aksi : "))
    if pilihan == 1:
        print("""
 ID  | Type                | ATK Power    | DEF Power     | HP      |""")
        for i in range (len(monster_db["type"])):
                        print(f"""
 {monster_db["id"][i]}  | {monster_db["type"][i]}                | {monster_db["atk_power"][i]}    | {monster_db["def_power"][i]}     | {monster_db["hp"][i]}      |""")
    elif pilihan == 2:
        addType = ''
        addATKP = ''
        addDEFP = ''
        addHP = ''
        print("Memulai pembuatan monster baru")
        added = False
        while added == False:
            if addType == '':
                addType = input(">>> Masukkan Type / Nama : ")
            elif addType not in monster_db["type"]:
                  monster_db["id"].append(last(monster_db["id"])+1)
                  monster_db["type"].append(addType)
                  added = True
            else:
                print("Nama sudah terdaftar, coba lagi")


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
