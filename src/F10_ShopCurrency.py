"""
F10 - Shop & Currency
19623296 / Muhammad Ra'if Alkautsar
"""

from global_var import *
from src.x01 import *

#currency = 1000 # SAMPEL. PLACEHOLDER VALUE
#user = 2

def add_monster(user_id, monster_index, enemy_level, monster_inv_db):
    # Pada fungsi ini, akan dilakukan insertion ke database monster inventory.
    # Fungsi dibuat seperti di bawah supaya tidak terjadi kesalahan pada fungsi saat mencoba mengakses variabel global.
    # Iterator dan tiga variabel untuk menyetor nilai sementara diinisialisasi terlebih dahulu.
    i = 0
    temp_user = int(user_id)
    temp_index = int(monster_index + 1)
    temp_level = int(enemy_level)
    # Indeks terakhir monster pemain dicari terlebih dahulu supaya monster dapat ditambahkan setelahnya.
    while monster_inv_db["user_id"][i] <= user_id and i < len(monster_inv_db["user_id"]):
        i += 1
    # Setelah ketemu, monster ditambahkan ke indeks setelah indeks terakhir monster pemain.
    # Monster yang tadinya berada di posisi tersebut akan disimpan terlebih dahulu di variabel sementara.
    (monster_inv_db["user_id"][i], temp_user) = (temp_user, monster_inv_db["user_id"][i])
    (monster_inv_db["monster_id"][i], temp_index) = (temp_index, monster_inv_db["monster_id"][i])
    (monster_inv_db["level"][i], temp_level) = (temp_level, monster_inv_db["level"][i])
    i += 1 
    # Setelah itu, kita "mundurkan" semua elemen yang ada setelahnya dengan cara menukar-nukar.
    while i < (len(monster_inv_db["user_id"])):
        
        (monster_inv_db["user_id"][i], temp_user) = (temp_user, monster_inv_db["user_id"][i])
        (monster_inv_db["monster_id"][i], temp_index) = (temp_index, monster_inv_db["monster_id"][i])
        (monster_inv_db["level"][i], temp_level) = (temp_level, monster_inv_db["level"][i])
        i += 1
    # Setelah sampai di indeks terakhir, gunakan append supaya tidak out-of-range.
    monster_inv_db["user_id"].append(temp_user)
    monster_inv_db["monster_id"].append(temp_index)
    monster_inv_db["level"].append(temp_level)
    return(monster_inv_db)

def add_item(user_id, item, item_inv_db):
    # NB: JIKA AKAN MENGGUNAKAN FUNGSI INI DI DALAM SEBUAH PROSEDUR, TOLONG TULIS from global_var import item_inv_db TERLEBIH DAHULU 
    # Pada fungsi ini, akan dilakukan insertion ke database item inventory.
    # Fungsi dibuat seperti di bawah supaya tidak terjadi kesalahan pada fungsi saat mencoba mengakses variabel global.
    # Iterator dan tiga variabel untuk menyetor nilai diinisialisasi terlebih dahulu.
    i = 0
    temp_user = int(user_id)
    temp_type = str(item)
    temp_quantity = 1
    found = False # Variabel untuk menentukan apakah pemain memiliki item yang dimaksud atau tidak?
    # Indeks item pemain dicari terlebih dahulu.
    while item_inv_db["user_id"][i] != user_id and item_inv_db["user_id"][i] <= user_id and i < len(item_inv_db["user_id"]):
        i += 1
    # Setelah ketemu, dicari item yang dimaksud.
    while item_inv_db["user_id"][i] == user_id and found != True: 
        if item_inv_db["type"][i] == item:
            item_inv_db["quantity"][i] += 1
            found = True
        i += 1
    if found != True:
        (item_inv_db["user_id"][i], temp_user) = (temp_user, item_inv_db["user_id"][i])
        (item_inv_db["type"][i], temp_type) = (temp_type, item_inv_db["type"][i])
        (item_inv_db["quantity"][i], temp_quantity) = (temp_quantity, item_inv_db["quantity"][i])
        i += 1
        while i < (len(item_inv_db["user_id"])):
            (item_inv_db["user_id"][i], temp_user) = (temp_user, item_inv_db["user_id"][i])
            (item_inv_db["type"][i], temp_type) = (temp_type, item_inv_db["type"][i])
            (item_inv_db["quantity"][i], temp_quantity) = (temp_quantity, item_inv_db["quantity"][i])
            i += 1
        # Setelah itu, kita "mundurkan" semua elemen yang ada setelahnya dengan cara menukar-nukar.
        # Setelah sampai di indeks terakhir, gunakan append supaya tidak out-of-range.
        item_inv_db["user_id"].append(temp_user)
        item_inv_db["type"].append(temp_type)
        item_inv_db["quantity"].append(temp_quantity)
    return(item_inv_db)

def remove_item(index, item_inv_db):
    i = 0
    temp_user = item_inv_db["user_id"][index]
    temp_type = item_inv_db["type"][index]
    temp_quantity = item_inv_db["quantity"][index]
    while item_inv_db["user_id"][i] != item_inv_db["user_id"][index] and item_inv_db["user_id"][i] <= item_inv_db["user_id"][index] and i < len(item_inv_db["user_id"]):
        i += 1
    while item_inv_db["user_id"][i] == item_inv_db["user_id"][index]: 
        if i == index:
            break
        i += 1
    while i < (len(item_inv_db["user_id"])-1):
        (item_inv_db["user_id"][i], temp_user) = (temp_user, item_inv_db["user_id"][i+1])
        (item_inv_db["type"][i], temp_type) = (temp_type, item_inv_db["type"][i+1])
        (item_inv_db["quantity"][i], temp_quantity) = (temp_quantity, item_inv_db["quantity"][i+1])
        i += 1
    item_inv_db["user_id"] = item_inv_db["user_id"][:-1]
    item_inv_db["type"] = item_inv_db["type"][:-1]
    item_inv_db["quantity"] = item_inv_db["quantity"][:-1]
    return(item_inv_db)

def monster_shop_list(monster_shop_db, monster_db):
    print(f"{"ID":<2} | {"Monster":<10} | {"ATK":<5} | {"DEF":<5} | {"HP":<5}")
    for i in range(len(monster_shop_db["monster_id"])):
        monster_idx = get_idx(monster_shop_db["monster_id"][i], monster_db["id"])
        print(f"{monster_db["id"][monster_idx]} | {monster_db["type"][monster_idx]:<10} | {monster_db["atk_power"][monster_idx]:<5} | {monster_db["def_power"][monster_idx]:<5} | {monster_db["hp"][monster_idx]:<5}")

def item_shop_list(item_shop_db):
    print(f"{"Type":<12} | {"Stock":<4} | {"Price":<4}")
    for i in range(len(item_shop_db["type"])):
        print(f"{item_shop_db["type"][i].capitalize():<12} | {item_shop_db["stock"][i]:<5} | {item_shop_db["price"][i]:<5}")

def monster_shop(monster_inv_db, monster_shop_db, monster_db, oc, user_id):
    monster_shop_list(monster_shop_db, monster_db)
    while True:
        choice = input("Ketik ID monster yang ingin kamu beli. (Ketik 'exit' untuk kembali): ")
        if choice == "exit":
            print("Kamu kembali ke menu ...")
            break
        elif is_numerical(choice) == False:
            print("Pilihan bukanlah angka!")
        else:
            choice = int(choice)
            if choice > (len(monster_shop_db) + 1) or choice < 1:
                print("ID yang kamu pilih tidak ada!")
            elif oc < monster_shop_db["price"][choice - 1]:
                print("Uang kamu tidak mencukupi untuk membeli monster tersebut!")
            else: 
                print(f"Kamu membeli monster {monster_db["type"][choice-1]}.")
                monster_inv_db = add_monster(user_id, choice-1, 1, monster_inv_db)
    return monster_inv_db, monster_shop_db, monster_db, oc

def item_shop(item_inv_db, item_shop_db, oc, user_id):
    item_shop_list(item_shop_db)
    while True:
        choice = input("Ketik nama item yang ingin kamu beli. (Ketik 'exit' untuk kembali): ").lower()
        if choice == "exit":
            print("Kamu kembali ke menu ...")
            break
        elif is_numerical(choice) == True:
            print("Tulis pilihan anda dalam bentuk teks!")
        elif choice != "strength" and choice != "resilience" and choice != "healing" and choice != "monsterball":
            print("Pilihan tidak tersedia!")
        elif oc < item_shop_db["price"][get_idx(choice, item_shop_db["type"])]:
            print("Uang kamu tidak mencukup untuk membeli monster tersebut!")
        else:
            if choice != "monsterball":
                print(f"Kamu membeli potion {choice}.")
            else: 
                print("Kamu membeli monster ball.")    
            item_inv_db = add_item(user_id, choice, item_inv_db)
    return item_inv_db, item_shop_db, oc

def shop(monster_inv_db, item_inv_db, monster_shop_db, item_shop_db, monster_db, oc, user_id):
    print("Selamat datang di Warkom (Warung Komplit) Pak Yanto!")
    while True:
        pilihan = input("Pak Yanto: 'Mau beli apa? (monster/item)' ")
        if pilihan == "monster":
            monster_inv_db, monster_shop_db, monster_db, oc = monster_shop(monster_inv_db, monster_shop_db, monster_db, oc, user_id)
            break
        elif pilihan == "item":
            item_inv_db, item_shop_db, oc = item_shop(item_inv_db, item_shop_db, oc, user_id)
            break
        else: 
            print("Pak Yanto: 'Yang itu mah gak ada, euy!'")
    return (monster_inv_db, item_inv_db, monster_shop_db, item_shop_db, oc)

"""

DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.

""" 
