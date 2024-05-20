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
    found = False
    i = 0
    j = 1
    while i < len(item_inv_db['user_id']) and item_inv_db['user_id'][i] != user_id:
        i += 1
    while i < len(item_inv_db['user_id']) and item_inv_db['user_id'][i] == user_id:
        found = True
        print(f"{j}. {(item_inv_db['type'][i]).title()} (Quantity: {item_inv_db['quantity'][i]})")
        i += 1
        j += 1
    if not found:
        print("Tidak mempunyai item!")

def show_monsters(monster_inv_db, monster_db, user_id):
    found = False
    i = 0
    j = 1
    while i < len(monster_inv_db['user_id']) and monster_inv_db['user_id'][i] != user_id:
        i += 1
    while i < len(monster_inv_db['user_id']) and monster_inv_db['user_id'][i] == user_id:
        found = True
        print(f"{j}. {get_monster(monster_inv_db['monster_id'][i], monster_inv_db['level'][i], monster_db)}")
        i += 1
        j += 1
    if not found:
        print("Tidak mempunyai monster!")

def get_start_index(db, user_id) -> int: # Fungsi ini dibuat untuk mendapatkan indeks pertama dari barang pengguna, digunakan pada monster inventory dan item inventory.
    i = 0
    while i < len(db['user_id']) and db['user_id'][i] != user_id:
        i += 1
    return(i)

def show_inventory(item_inv_db, monster_inv_db, monster_db, user_id):
    os
    print("Potion yang kamu miliki: ")
    show_items(item_inv_db, user_id)
    print("Monster yang kamu miliki:")
    show_monsters(monster_inv_db, monster_db, user_id)

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
"""
