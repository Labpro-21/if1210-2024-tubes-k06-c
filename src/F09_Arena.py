"""
F09 - Arena
19623076 Daniel A. M. Sipayung
"""

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
# from F08_Battle import *
from F00_RandomNumberGenerator import *
def arena ():
    print(""" 
Selamat datang di Arena!!
          
================ MONSTER LIST ================""")
    MonAvai = 1
    for i in monster_db["type"]:
        print(f"{MonAvai}. {i}")
        MonAvai+=1
    numAvai = False
    while numAvai == False:
        monstRand = monster_db["type"][rng(0,len(monster_db["type"]),int(working_time))]
        pilihan = int(input("""
Pilih monster untuk bertarung!
>>> """))
        if pilihan > len(monster_db["type"]):
            print("Pilihan nomor tidak tersedia!")
        else:
            numAvai = True
    
    print(f"""      
            
          /\----/\_
         /         \   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \  |   |   |
         |  |   |   |
          \._\   \._\    

RAWRRRRRRR, (Nama Agent) mengeluarkan monster {monster_db["type"][pilihan-1]}!!!
Name      : {monster_db["type"][pilihan-1]}
ATK Power : {monster_db["atk_power"][pilihan-1]}
DEF Power : {monster_db["def_power"][pilihan-1]}
HP        : {monster_db["hp"][pilihan-1]}
Level     : LAGI PROSES""")
     #{monster_inv_db["level"][get_idx()]}
    # BERMASALAH DI PEMANGGILAN LEVEL
    
    time.sleep(5)

    menang = True # HASIL RETURN DARI BATTLE
    count= 0
    while menang == True:

        count+=1
        print(f""" 
              
============= STAGE {count} =============


           _/\----/\
          /         \     /         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \  |  |
        /   `^^^^^'    \ |  |
      ./  /|            \|  |_
     /   / |         |\__     /
     \  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__
RAWRRR, Monster {monstRand} telah muncul !!!
   # battle()

    
    """)
        menang = input(">>>")
        if menang == True:
            print(f"Selamat, Anda berhasil mengalahkan monster {monstRand} !!!")
        else:
            print(f"""
Yahhh, Anda dikalahkan monster {monstRand}. Jangan menyerah, coba lagi !!!

GAME OVER! Sesi latihan berakhir pada stage {count}!

                  """)
        if count == 1 and menang == True:
            print("uang tambah 25")
        if count == 2 and menang == True:
            print("uang tambah 50")
        if count == 3 and menang == True:
            print("uang tambah 100")
        if count == 4 and menang == True:
            print("uang tambah 125")
        if count == 5 and menang == True:
            print("uang tambah 150")

        menang = False






# MONSTER pilihan awal masih menggunakan monster db bukan monster milik user
# PERMASALAHAN PEMANGGILAN LEVEL
# Nama logged in blm ada
# tambah uang blm lengkap










"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
"""
