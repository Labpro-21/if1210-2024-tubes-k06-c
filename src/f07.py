"""
F07 - Inventory
19623296 Muhammad Ra'if Alkautsar
"""
from x01 import *
from f14 import *

current_user = 3 # sampel

def getMonster(i): # mengambil data monster 
    monsterList = load("data/monster.csv")
    return(f"{monsterList["type"][i]} (ATK Power: {monsterList["atk_power"][i]} | DEF Power: {monsterList["def_power"][i]} | HP: {monsterList["hp"][i]})")

def showItems():
    itemList = load("data/item_inventory.csv")
    i = 0
    if i < len(itemList['user_id']):
        while itemList['user_id'][i] != current_user:
            i += 1
            pass
        while itemList['user_id'][i] == current_user:
            i += 1
            print(f"{(itemList["type"][i]).title()} (Quantity: {itemList["quantity"][i]})")

def showMonsters():
    monsterInvList = load("data/monster_inventory.csv")
    i = 0
    if i < len(monsterInvList['user_id']):
        while monsterInvList['user_id'][i] != current_user:
            i += 1
            pass
        while monsterInvList['user_id'][i] == current_user:
            i += 1
            print(f"{getMonster(monsterInvList['monster_id'][i])}")

def showInventory():
    print("Potion yang kamu miliki: ")
    showItems()
    print("Monster yang kamu miliki:")
    showMonsters()

showInventory()

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
"""