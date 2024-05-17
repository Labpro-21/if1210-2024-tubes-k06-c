"""
F07 - Inventory
19623296 Muhammad Ra'if Alkautsar
"""
from src.x01 import *
from src.F14_Load import *
from src.F05_Monster import *

current_user = 3 # sampel

from global_var import *
def get_monster(i, lv): # mengambil data monster 
    monster_to_get = attribute_monster(i, lv, monster_db)
    return(f"{monster_to_get[0]} (ATK Power: {monster_to_get[1]} | DEF Power: {monster_to_get[2]} | HP: {monster_to_get[3]})")

def show_items():
    i = 0
    j = 1
    while item_inv_db['user_id'][i] != current_user:
        i += 1
        pass
    while item_inv_db['user_id'][i] == current_user:
        print(f"{j}. {(item_inv_db["type"][i]).title()} (Quantity: {item_inv_db["quantity"][i]})")
        i += 1
        j += 1

def show_monsters():
    i = 0
    j = 1
    while monster_inv_db['user_id'][i] != current_user:
        i += 1
        pass
    while monster_inv_db['user_id'][i] == current_user:
        print(f"{j}. {get_monster(monster_inv_db['monster_id'][i], monster_inv_db['level'][i])}")
        i += 1
        j += 1

def get_start_index(db, current_user) -> int: # Fungsi ini dibuat untuk mendapatkan indeks pertama dari barang pengguna, digunakan pada monster inventory dan item inventory.
    i = 0
    while db['user_id'][i] != current_user:
        i += 1
    j = i
    return(j)

def show_inventory():
    print("Potion yang kamu miliki: ")
    show_items()
    print("Monster yang kamu miliki:")
    show_monsters()

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
"""
