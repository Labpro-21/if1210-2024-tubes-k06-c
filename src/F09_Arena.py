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