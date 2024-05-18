"""
F08 - Battle
19623296 Muhammad Ra'if Alkautsar
"""

# ALPHA STATE / BELUM BERFUNGSI SEPENUHNYA / BELUM RAPI / BELUM EFISIEN

from src.x01 import *
from src.F00_RandomNumberGenerator import *
from src.F14_Load import *
from src.B03_MonsterBall import *
from src.F05_Monster import *
from src.F06_Potion import *
from src.F07_Inventory import *
from colorama import *
from global_var import *

# enemy_level = 3 # SAMPEL
# user = 3 # SAMPEL

def show_state(type1, hp1, atk1, def1, type2, hp2, atk2, def2):
    print(f"{type1:<17} | {type2:>17}")
    print(f"HP    / ATK / DEF | HP   / ATK / DEF")
    print(f"{hp1:<5} / {atk1:<3} / {def1:<3} | {hp2:>5} / {atk2:>3} / {def2:>3}")

def use_potion(item_inv_db, user_id, user_idx, your_monster, your_atk, your_def, your_hp):
    print("Ramuan-ramuan yang kamu miliki saat ini: ")
    show_items(item_inv_db, user_id)
    while True:
        pot_index = int(input("Ramuan apa yang ingin kamu pilih? (Pilih dengan angka)")) - 1 + get_start_index(item_inv_db, user_id)
        if item_inv_db["quantity"][pot_index] == 0:
            print("Ramuan habis!")
        else: 
            if item_inv_db["type"][pot_index] == "strength":
                your_atk = strength_potion(your_atk)
                break
            elif item_inv_db["type"][pot_index] == "resilience":
                your_def = resilience_potion(your_def)
                break
            elif item_inv_db["type"][pot_index] == "healing":
                your_hp = healing_potion(your_hp, your_monster[3])
                break
            else:
                print("Ramuan tidak valid!")
            return(item_inv_db, your_atk, your_def, your_hp)

def battle(monster_db, monster_inv_db, user_id, enemy_level, item_inv_db, oc):
    random_index = int(rng(0, len(monster_db['id']), int(time.time()))) # Meminta index untuk monster random
    # Inisialisasi Monster Musuh
    enemy_monster = attribute_monster(random_index + 1, enemy_level, monster_db)
    enemy_type = enemy_monster[0]
    enemy_atk = enemy_monster[1]
    enemy_def = enemy_monster[2]
    enemy_hp = enemy_monster[3]
    print(f"{enemy_type} mendekat!")
    print(f"HP: {enemy_hp}. DEF: {enemy_def}. ATK: {enemy_atk}.")

    # Inisialisasi Monster Pemain
    print("Monster-monster yang kamu miliki saat ini: ")
    show_monsters()
    your_index = int(input("Monster apa yang ingin kamu pilih? ")) - 1 + get_start_index(monster_inv_db, user_id)
    your_monster_idx = monster_inv_db["monster_id"][your_index]
    your_monster = attribute_monster(your_monster_idx, monster_inv_db["level"][your_index], monster_db)
    your_level = monster_inv_db["level"][your_index]
    your_type = your_monster[0]
    your_atk = your_monster[1]
    your_def = your_monster[2]
    your_hp = your_monster[3]
    print(f"Kamu memilih {your_type}.")
    print(f"HP: {your_hp}. DEF: {your_def}. ATK: {your_atk}.")

    # Memasuki loop utama battle
    isBattle = True
    while isBattle == True:
        while True:
            print("┌─ Pilihan Aksi")
            print("├ 1. Attack")
            print("├ 2. Use Potion")
            print("├ 3. Monsterball")
            print("└ 4. Quit")
            action = input("Apa yang akan kamu lakukan? (Ketik pilihanmu!) ") 
            
            match action:
                case "1":
                    enemy_hp = enemy_hp - atk_result(your_atk, enemy_def)
                    break
                case "2":
                    item_inv_db, your_atk, your_def, your_hp = use_potion(item_inv_db, user_id, your_monster, your_atk, your_def, your_hp)
                    break
                case "3":
                    if monsterball(your_level):
                        print("Monster berhasil tertangkap!")
                        monster_inv_db = add_monster(user_id, random_index, enemy_level, monster_inv_db)
                        enemy_hp = 0
                    else: 
                        print("Monster lepas!")
                    break

                case "4": 
                    isBattle == False
                    print("Kamu berhasil kabur ...")
                    break
                case _:
                    print("Pilihan tidak valid! \n")
        
        your_hp = your_hp - atk_result(enemy_atk, your_def)

        if enemy_hp <= 0:
            print("Selamat, kamu menang!")
            isBattle = False
        elif your_hp <= 0: 
            print("Monstermu habis. Kamu kalah.")
            isBattle = False
        else: 
            print(f"Pertarungan terus berlangsung! \n HP Monster-mu: {your_hp} \n HP Monster Musuh: {enemy_hp}")
        return(monster_inv_db, item_inv_db, oc)

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
