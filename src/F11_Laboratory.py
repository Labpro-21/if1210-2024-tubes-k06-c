"""
F11 - Laboratory
16523146 Sacca 
19623296 Muhammad Ra'if Alkautsar
"""
from global_var import *
from src.F07_Inventory import *

# Kode di sini
def upgrade_monster(monster_inv_db, monster_db, i, oc):
    if monster_inv_db['level'][i] >= 5:
        print("Maaf, monster yang Anda pilih sudah memiliki level maksimum.")
        return oc

    monster_index_in_monster_db = monster_inv_db["monster_id"][i] - 1
    monster_name = monster_db['type'][monster_index_in_monster_db]
    upgrade_costs = [300, 500, 800, 1000]
    current_level = monster_inv_db['level'][i]
    upgrade_cost = upgrade_costs[current_level - 1]
    print(f"\n{monster_name} akan di-upgrade ke level {current_level + 1}.")
    print(f"Harga untuk melakukan upgrade {monster_name} adalah {upgrade_cost} OC.")

    if oc >= upgrade_cost:
        confirm = input(">>> Lanjutkan upgrade (Y/N): ")
        if confirm.lower() == 'y':
            monster_inv_db['level'][i] += 1
            oc -= upgrade_cost
            print(f"Selamat, {monster_name} berhasil di-upgrade ke level {current_level + 1}!")
        elif confirm.lower() == 'n':
            print("Upgrade dibatalkan.")
        else:
            print("Pilihan tidak valid. Silakan masukkan Y atau N.")
    else:
        print("Maaf, OC Anda tidak mencukupi untuk melakukan upgrade.")
    return monster_inv_db, oc

def laboratory(user_id, monster_db, monster_inv_db, oc):
    while True:
        print("\nSelamat datang di Lab Dokter Asep !!!\n")
        
        print("============ MONSTER LIST ============")
        print(show_monsters(monster_inv_db, monster_db, user_id))

        print("\n============ UPGRADE PRICE ============")
        print("1. Level 1 -> Level 2: 300 OC")
        print("2. Level 2 -> Level 3: 500 OC")
        print("3. Level 3 -> Level 4: 800 OC")
        print("4. Level 4 -> Level 5: 1000 OC")

        user_input = input(">>> Pilih monster (atau ketik 'exit' untuk keluar): ")
        if user_input == 'exit':
            break
        elif user_input.isdigit():
            user_input = int(user_input)
            i = int(user_input - 1 + get_start_index(monster_inv_db, user_id))
            if 1 <= i + 1 <= len(monster_db["type"]):
                monster_inv_db, oc = upgrade_monster(monster_inv_db, monster_db, i, oc)
            else:
                print("Pilihan tidak valid, silakan pilih nomor monster yang valid.")
        else:
            print("Pilihan tidak valid, silakan pilih nomor monster yang valid.")
        
        return monster_inv_db, oc
