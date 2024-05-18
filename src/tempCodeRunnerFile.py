import time
start = time.time()

from F00_RandomNumberGenerator import *
from  F14_Load import *
from global_var import *
from F10_ShopCurrency import add_monster


# Define the jackpot function as before
def jackpot(username: str) -> None:
    user = username
    current_user = get_idx(user, user_db["username"])
    owca_coins = user_db["oc"][current_user]

    if owca_coins < 1000:
        print("Maaf, anda tidak memiliki cukup OC untuk bermain JACKPOT.")
        return
    user_db["oc"][current_user] -= 1000

    items = ["Topi", "Pedang", "Koin", "Potion", "Monster"]
    item_values = [50, 100, 200, 300, 500]

    item1_idx = rng(0, len(items), int(working_time))
    item2_idx = rng(0, len(items), int(working_time))
    item3_idx = rng(0, len(items), int(working_time))
    
    item1 = items[item1_idx]
    item2 = items[item2_idx]
    item3 = items[item3_idx]

    print(f"Anda Mendapatkan:\n{item1} | {item2} | {item3}")

    if item1 == item2 == item3:
        monster = monster_db["type"][item2_idx]
        enemy_level = 1
        add_monster (current_user, item2_idx, enemy_level, monster_inv_db)
        print(f"JACKPOT!!! Selamat, Anda mendapatkan monster {monster}.")
    else:
        item1_value = item_values[item1_idx]
        item2_value = item_values[item2_idx]
        item3_value = item_values[item3_idx]

        total_oc = item1_value + item2_value + item3_value
        user_db["oc"][current_user] += total_oc
        print(f"Didapat {total_oc} OC.")
    


# Call the jackpot function 
jackpot("Asep_Spakbor")
