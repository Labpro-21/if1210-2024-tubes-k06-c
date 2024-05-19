"""
F09 - Arena
19623076 Daniel A. M. Sipayung
19623296 Muhammad Ra'if Alkautsar
"""

# Kode di sini
from src.F05_Monster import *
import sys, os
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(parent_path, 'data')
sys.path.append(parent_path)
sys.path.append(data_path)
# Memuat file .csv yang diperlukan
from global_var import *
from src.x01 import *
# from F08_Battle import *
from src.F00_RandomNumberGenerator import *
from src.F08_Battle import *

def arena(monster_db, monster_inv_db, user_id, item_inv_db, oc):
    total_dealt = 0
    total_received = 0
    reward = 0
    stage = 1
    defeat = False
    while defeat == False and stage <= 5:
        monster_inv_db, item_inv_db, oc, victory, damage_dealt, damage_received = battle(monster_db, monster_inv_db, user_id, stage, item_inv_db, oc, "arena")
        
        total_dealt += damage_dealt
        total_received += damage_received

        if victory == True:
            if stage == 1:
                reward += 30 
            elif stage == 2:
                reward += 50
            elif stage == 3:
                reward += 100
            elif stage == 4:
                reward += 200
            elif stage == 5:
                reward += 400
            stage += 1
        else:
            print("Yah, kamu kalah.")
            defeat = True
    
    if defeat == False:
        print("Selamat, kamu berhasil menyelesaikan arena!")
    else:
        print("Kamu mencapai stage", stage, "dari 5.")

    print(f"Kamu mendapatkan {reward} OC.")
    print(f"Total damage yang kamu berikan: {total_dealt}")
    print(f"Total damage yang kamu terima: {total_received}")
    return(monster_inv_db, item_inv_db, oc + reward)
        
        



# def arena ():
#     print(""" 
# Selamat datang di Arena!!
          
# ================ MONSTER LIST ================""")
#     MonAvai = 1
#     for i in monster_db["type"]:
#         print(f"{MonAvai}. {i}")
#         MonAvai+=1
#     numAvai = False
#     while numAvai == False:
#         monstRand = monster_db["type"][rng(0,len(monster_db["type"]),int(working_time))]
#         pilihan = int(input("""
# Pilih monster untuk bertarung!
# >>> """))
#         if pilihan > len(monster_db["type"]):
#             print("Pilihan nomor tidak tersedia!")
#         else:
#             numAvai = True
    
#     print(f"""      
            
#           /\----/\_
#          /         \   /|
#         |  | O    O | / |
#         |  | .vvvvv.|/  /
#        /   | |     |   /
#       /    | `^^^^^   /
#      | /|  |         /
#       / |    ___    |
#          \  |   |   |
#          |  |   |   |
#           \._\   \._\    

# RAWRRRRRRR, (Nama Agent) mengeluarkan monster {monster_db["type"][pilihan-1]}!!!
# Name      : {monster_db["type"][pilihan-1]}
# ATK Power : {monster_db["atk_power"][pilihan-1]}
# DEF Power : {monster_db["def_power"][pilihan-1]}
# HP        : {monster_db["hp"][pilihan-1]}
# Level     : LAGI PROSES""")
#      #{monster_inv_db["level"][get_idx()]}
#     # BERMASALAH DI PEMANGGILAN LEVEL
    
#     time.sleep(5)

#     menang = True # HASIL RETURN DARI BATTLE
#     count= 0
#     while menang == True:

#         count+=1
#         print(f""" 
              
# ============= STAGE {count} =============


#            _/\----/\
#           /         \     /         |  O    O   |   |  |
#          |  .vvvvv.  |   |  |
#          /  |     |   \  |  |
#         /   `^^^^^'    \ |  |
#       ./  /|            \|  |_
#      /   / |         |\__     /
#      \  /  |         |   |__|
#       `'   |  _      |
#         _.-'-' `-'-'.'_
#    __.-'               '-.__
# RAWRRR, Monster {monstRand} telah muncul !!!
#    # battle()

    
#     """)
#         menang = input(">>>")
#         if menang == True:
#             print(f"Selamat, Anda berhasil mengalahkan monster {monstRand} !!!")
#         else:
#             print(f"""
# Yahhh, Anda dikalahkan monster {monstRand}. Jangan menyerah, coba lagi !!!

# GAME OVER! Sesi latihan berakhir pada stage {count}!

#                   """)
#         if count == 1 and menang == True:
#             print("uang tambah 25")
#         if count == 2 and menang == True:
#             print("uang tambah 50")
#         if count == 3 and menang == True:
#             print("uang tambah 100")
#         if count == 4 and menang == True:
#             print("uang tambah 125")
#         if count == 5 and menang == True:
#             print("uang tambah 150")

#         menang = False






# MONSTER pilihan awal masih menggunakan monster db bukan monster milik user
# PERMASALAHAN PEMANGGILAN LEVEL
# Nama logged in blm ada
# tambah uang blm lengkap










"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
"""
