"""
FB03 - JACKPOT!
16523146 SACCA 
"""
from F00_RandomNumberGenerator import *
from  F14_Load import *
from global_var import *
from F10_ShopCurrency import add_monster

def jackpot(username: str) -> None:
    # Cek OC penguna
    user = username
    current_user = get_idx(user, user_db["username"])
    owca_coins = user_db["oc"][current_user]

    # Cek jika oc cukup untuk main
    if owca_coins < 1000:
        print("Maaf, anda tidak memiliki cukup OC untuk bermain JACKPOT.")
        return
    # Kurangi OC untuk main
    user_db["oc"][current_user] -= 1000

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
        monster = monster_db["type"][item2_idx]
        # Buat jadi level 1
        enemy_level = 1
        #  Tambahkan monster ke user inventory
        add_monster (current_user, item2_idx, enemy_level, monster_inv_db)
        # Print ouput
        print(f"JACKPOT!!! Selamat, Anda mendapatkan monster {monster}.")
    else:
        # Hitung oc yang dimenangkan
        item1_value = item_values[item1_idx]
        item2_value = item_values[item2_idx]
        item3_value = item_values[item3_idx]
        total_oc = item1_value + item2_value + item3_value
        # Tambhakan oc ke oc pengguna
        user_db["oc"][current_user] += total_oc
        # Print output
        print(f"Didapat {total_oc} OC.")

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
