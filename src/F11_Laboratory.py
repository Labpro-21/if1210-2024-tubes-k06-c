"""
F11 - Laboratory
16523146 Sacca 
"""
from global_var import *

# Kode di sini
def upgrade_monster(monster: str, oc, db = monster_db):
    monster_idx = get_idx(monster, db["type"])
    monster_name = db["type"][monster_idx]
    if db['level'][monster_idx] >= 5:
        print("Maaf, monster yang Anda pilih sudah memiliki level maksimum.")
        return oc

    upgrade_costs = [300, 500, 800, 1000]
    current_level = db['level'][monster_idx]
    upgrade_cost = upgrade_costs[current_level - 1]
    print(f"\n{monster_name} akan di-upgrade ke level {current_level + 1}.")
    print(f"Harga untuk melakukan upgrade {monster_name} adalah {upgrade_cost} OC.")

    if oc >= upgrade_cost:
        confirm = input(">>> Lanjutkan upgrade (Y/N): ")
        if confirm.lower() == 'y':
            db['level'][monster_idx] += 1
            oc -= upgrade_cost
            current_level += 1
            print(f"Selamat, {monster_name} berhasil di-upgrade ke level {current_level}!")
        elif confirm.lower() == 'n':
            print("Upgrade dibatalkan.")
        else:
            print("Pilihan tidak valid. Silakan masukkan Y atau N.")
    else:
        print("Maaf, OC Anda tidak mencukupi untuk melakukan upgrade.")
    return oc

def laboratory(user_id, monsters, owca_coins):
    while True:
        print("\nSelamat datang di Lab Dokter Asep !!!\n")
        
        print("============ MONSTER LIST ============")
        print(show_monster_inv(user_id))

        print("\n============ UPGRADE PRICE ============")
        print("1. Level 1 -> Level 2: 300 OC")
        print("2. Level 2 -> Level 3: 500 OC")
        print("3. Level 3 -> Level 4: 800 OC")
        print("4. Level 4 -> Level 5: 1000 OC")

        user_input = input(">>> Pilih monster (atau ketik 'exit' untuk keluar): ")
        if user_input == 'exit':
            break
        elif user_input.isdigit():
            i = int(user_input) - 1
            if 1 <= i + 1 <= len(monsters):
                owca_coins = upgrade_monster(monsters, i, owca_coins)
            else:
                print("Pilihan tidak valid, silakan pilih nomor monster yang valid.")
        else:
            print("Pilihan tidak valid, silakan pilih nomor monster yang valid.")


def get_monster(i, monsters = monster_db): # mengambil data monster dan level
    return(monsters["type"][i], monsters["level"][i])


def show_monster_inv(user_id, monsters_inv = monster_inv_db, monsters = monster_db):
    count = 1
    for i in range(len(monsters_inv['user_id'])):
        if monsters_inv['user_id'][i] == user_id:
            monster = get_monster(i)
            print(f"{count}. {monster[0]} (Level: {monster[1]})")
            count += 1
        

# coba2
""" current_user = get_idx('B4ngk1dd0ssss', user_db["username"])
user_id = user_db["id"][current_user]
monsters = showMonsters()
owca_coins = user_db["oc"][current_user]
laboratory(monsters,owca_coins) """
"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
