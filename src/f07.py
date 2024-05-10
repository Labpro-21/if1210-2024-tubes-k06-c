"""
F07 - Inventory
19623296 Muhammad Ra'if Alkautsar
"""
from x01 import *
from x02 import *

current_user = 3 # sampel

def getMonster(i): # mengambil data monster 
    monsterList = csv_parser("data/monster.csv", "id")
    return(f"Type: {monsterList["type"][i]} | ATK Power: {monsterList["atk_power"][i]} | DEF Power: {monsterList["def_power"][i]} | HP: {monsterList["hp"][i]} ")

def showItems():
    itemList = csv_parser_noid("data/item_inventory.csv")
    i = 0
    if i < len(itemList):
        while itemList[i]['user_id'] != current_user:
            i += 1
            pass
        while itemList[i]['user_id'] == current_user:
            i += 1
            print(f"{itemList[i]["type"]} (Quantity: {itemList[i]["quantity"]})")

def showMonsters():
    monsterInvList = csv_parser_noid("data/monster_inventory.csv")
    i = 0
    if i < len(monsterInvList):
        while monsterInvList[i]['user_id'] != current_user:
            i += 1
            pass
        while monsterInvList[i]['user_id'] == current_user:
            i += 1
            print(f"{getMonster(monsterInvList[i]['monster_id'])}")

def showInventory():
    print("Potion yang kamu miliki:")
    showItems()
    print("Monster yang kamu miliki:")
    showMonsters()

showInventory()

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
"""