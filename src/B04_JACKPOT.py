"""
FB03 - JACKPOT!
16523146 SACCA 
"""
from src.F00_RandomNumberGenerator import *
from src.F14_Load import *
from src.F10_ShopCurrency import add_monster
from global_var import *

def jackpot(oc, user_id, monster_db, monster_inv_db):
    # Cek jika oc cukup untuk main
    if oc < 200:
        print("Maaf, anda tidak memiliki cukup OC untuk bermain JACKPOT.")
        return(oc, monster_inv_db)
    # Kurangi OC untuk main
    oc -= 200

    # Harga item yang ada dan namanya
    items = ["Topi", "Pedang", "Koin", "Potion", "Monster"]
    item_values = [50, 100, 200, 300, 500]

    # Generate 3 item random
    item1_idx = rng(0, len(items), int(working_time))
    item2_idx = rng(0, len(items), int(working_time))
    item3_idx = rng(0, len(items), int(working_time))

    # Mnedapatakan nama item
    item1 = items[item1_idx]
    item2 = items[item2_idx]
    item3 = items[item3_idx]

    # Print nama item yang pengguna menang
    print(f"Anda Mendapatkan:\n{item1} | {item2} | {item3}")

    # Check jika pengguna mnedapat jackpot
    if item1 == item2 == item3:
        # Dapatakan nama monster
        random_monster_index = int(rng(0, len(monster_db["type"]), int(working_time)))
        monster = monster_db["type"][random_monster_index]
        # Buat jadi level 1
        monster_level = 1
        #  Tambahkan monster ke user inventory
        monster_inv_db = add_monster(user_id, random_monster_index, monster_level, monster_inv_db)
        # Print ouput
        print(f"JACKPOT!!! Selamat, Anda mendapatkan monster {monster}.")
    else:
        # Hitung oc yang dimenangkan
        item1_value = item_values[item1_idx]
        item2_value = item_values[item2_idx]
        item3_value = item_values[item3_idx]
        total_oc = item1_value + item2_value + item3_value
        # Tambhakan oc ke oc pengguna
        oc += total_oc
        # Print output
        print(f"Didapat {total_oc} OC.")
    
    return(oc, monster_inv_db)
"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
