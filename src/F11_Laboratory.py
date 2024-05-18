"""
F11 - Laboratory
16523146 Sacca 
"""
from src.global_var import *

# Kode di sini
def upgrade_monster(monsters, i, owca_coins):
    selected_monster = monsters[i]
    if selected_monster['level'] >= 5:
        print("Maaf, monster yang Anda pilih sudah memiliki level maksimum.")
        return owca_coins

    upgrade_costs = [300, 500, 800, 1000]
    current_level = selected_monster['level']
    upgrade_cost = upgrade_costs[current_level - 1]
    print(f"\n{selected_monster['name']} akan di-upgrade ke level {selected_monster['level'] + 1}.")
    print(f"Harga untuk melakukan upgrade {selected_monster['name']} adalah {upgrade_cost} OC.")

    if owca_coins >= upgrade_cost:
        confirm = input(">>> Lanjutkan upgrade (Y/N): ")
        if confirm.lower() == 'y':
            selected_monster['level'] += 1
            owca_coins -= upgrade_cost
            print(f"Selamat, {selected_monster['name']} berhasil di-upgrade ke level {selected_monster['level']}!")
        elif confirm.lower() == 'n':
            print("Upgrade dibatalkan.")
        else:
            print("Pilihan tidak valid. Silakan masukkan Y atau N.")
    else:
        print("Maaf, OC Anda tidak mencukupi untuk melakukan upgrade.")
    return owca_coins

def laboratory(monsters, owca_coins):
    while True:
        print("\nSelamat datang di Lab Dokter Asep !!!\n")
        
        print("============ MONSTER LIST ============")
        print(showMonsters())

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


def getMonster(i): # mengambil data monster dan level
    return(f"""{monster_db["type"][i]} (Level: {monster_inv_db["level"][i]})  """)


def showMonsters():

    i = 0
    if i < len(monster_inv_db['user_id']):
        while monster_inv_db['user_id'][i] != current_user:
            i += 1
            pass
        while monster_inv_db['user_id'][i] == current_user:
            i += 1
            return(f"{getMonster(monster_inv_db['monster_id'][i])}")

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
