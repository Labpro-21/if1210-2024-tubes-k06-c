"""
F07 - Inventory
19623296 Muhammad Ra'if Alkautsar
"""
from src.x01 import *
from src.F14_Load import *
from src.F05_Monster import *

# user_idx = 3 # sampel

from global_var import *
def get_monster(i, lv, monster_db): # mengambil data monster 
    monster_to_get = attribute_monster(i, lv, monster_db)
    return(f"{monster_to_get[0]} (ATK Power: {monster_to_get[1]} | DEF Power: {monster_to_get[2]} | HP: {monster_to_get[3]})")

def show_items(item_inv_db, user_id):
    i = 0
    j = 1
    while item_inv_db['user_id'][i] != user_id:
        i += 1
        pass
    while item_inv_db['user_id'][i] == user_id:
        print(f"{j}. {(item_inv_db["type"][i]).title()} (Quantity: {item_inv_db["quantity"][i]})")
        i += 1
        j += 1

def show_monsters(monster_inv_db, user_id):
    i = 0
    j = 1
    while monster_inv_db['user_id'][i] != user_id:
        i += 1
        pass
    while monster_inv_db['user_id'][i] == user_id:
        print(f"{j}. {get_monster(monster_inv_db['monster_id'][i], monster_inv_db['level'][i])}")
        i += 1
        j += 1

def get_start_index(db, user_id) -> int: # Fungsi ini dibuat untuk mendapatkan indeks pertama dari barang pengguna, digunakan pada monster inventory dan item inventory.
    i = 0
    while db['user_id'][i] != user_id:
        i += 1
    return(i)

def show_inventory(item_inv_db, monster_inv_db, user_id):
    print("Potion yang kamu miliki: ")
    show_items(item_inv_db, user_id)
    print("Monster yang kamu miliki:")
    show_monsters(monster_inv_db, user_id)

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
"""
