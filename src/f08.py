"""
F08 - Battle
19623296 Muhammad Ra'if Alkautsar
"""

# ALPHA STATE / BELUM BERFUNGSI SEPENUHNYA / BELUM RAPI / BELUM EFISIEN

from x01 import *
from f00 import *
from f14 import *
from colorama import *
from b03 import *
from f05 import *
from f06 import *
from f07 import *
from global_var import *

enemy_level = 3 # SAMPEL
user = 3

def use_potion():
    print("Ramuan-ramuan yang kamu miliki saat ini: ")
    show_items()
    pot_index = int(input("Ramuan apa yang ingin kamu pilih? (Pilih dengan angka)")) - 1 + get_start_index(item_inv_db, user)
    if item_inv_db["quantity"][pot_index] == 0:
        print("Ramuan habis!")
    else: 
        if item_inv_db["type"][pot_index] == "strength":
            your_atk = strength_potion(your_atk)
        elif item_inv_db["type"][pot_index] == "resilience":
            your_def = resilience_potion(your_def)
        else: # item_inv_db["type"][pot_index] == ""
            your_hp = healing_potion(your_hp, your_monster[3])

def battle():
    random_index = int(rng(0, len(monster_db['id']), time.time())) # Meminta index untuk monster random

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
    your_index = int(input("Monster apa yang ingin kamu pilih? ")) - 1 + get_start_index(monster_inv_db, user)
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
                    use_potion()
                    break
                case "3":
                    if monsterball(your_level):
                        print("Monster berhasil tertangkap!")
                        monster_caught()
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



battle()
"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""