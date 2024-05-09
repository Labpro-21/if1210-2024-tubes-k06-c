"""
F08 - Battle
19623296 Muhammad Ra'if Alkautsar
"""

# ALPHA STATE / BELUM BERFUNGSI SEPENUHNYA / BELUM RAPI / BELUM EFISIEN

from x01 import *
from f00 import *
from colorama import *


def attack(attacker : int, defender : int) -> int:
    defender["hp"] -= attacker["atk_power"]
    return(defender["hp"])

def battle():
    # Monster musuh dipilih melalui RNG. (Atribut dari monster.csv: id;type;atk_power;def_power;hp)
    enemyList = csv_parser("data/monster.csv")
    enemyMonster = enemyList[rng(0, len(enemyList))]
    print(f"Monster {enemyMonster["type"]} mendekat!")
    
    # Kita memilih monster melalui pilihan. (user_id;monster_id;level)
    # Fungsi untuk pemilihan monster masih dipertimbangkan, jadi akan digunakan sampel terlebih dahulu.
    yourList = [{'id':1, 'type':'Pikachow', 'atk_power':125, 'def_power':10, 'hp':600}] # SAMPEL
    yourMonster = yourList[0] # SAMPEL

    isBattle = True
    while isBattle == True:
        while True:
            print("┌─ Pilihan Aksi")
            print("├ 1. Attack")
            print("├ 2. Use Potion")
            print("└ 3. Quit")
            action = input("Apa yang akan kamu lakukan? (Ketik pilihanmu!) ") 
            
            match action:
                case "1":
                    enemyMonster["hp"] = attack(yourMonster, enemyMonster)
                    break
                case "2":
                    usePotion
                    break
                case "3": 
                    isBattle == False
                    print("Kamu berhasil kabur ...")
                    break
                case _:
                    print("Pilihan tidak valid! \n")
        
        yourMonster["hp"] = attack(enemyMonster, yourMonster)

        if enemyMonster["hp"] <= 0:
            print("Selamat, kamu menang!")
            isBattle = False
        elif yourMonster["hp"] <= 0: 
            print("Monstermu habis. Kamu kalah.")
            isBattle = False
        else: 
            print(f"Pertarungan terus berlangsung! \n HP Monster-mu: {yourMonster["hp"]} \n HP Monster Musuh: {enemyMonster["hp"]}")


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""