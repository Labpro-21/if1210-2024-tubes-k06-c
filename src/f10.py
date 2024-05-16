"""
F10 - Shop & Currency
19623296 / Muhammad Ra'if Alkautsar
"""

from global_var import *

currency = 1000 # SAMPEL. PLACEHOLDER VALUE
user = 2
def add_monster(user, index, enemy_level, monster_inv_db):
    # NB: JIKA AKAN MENGGUNAKAN FUNGSI INI DI DALAM SEBUAH PROSEDUR, TOLONG TULIS from global_var import monster_inv_db TERLEBIH DAHULU 

    # Pada fungsi ini, akan dilakukan insertion ke database monster inventory.
    # Fungsi dibuat seperti di bawah supaya tidak terjadi kesalahan pada fungsi saat mencoba mengakses variabel global.

    # Iterator dan tiga variabel untuk menyetor nilai sementara diinisialisasi terlebih dahulu.
    i = 0
    temp_user = int(user)
    temp_index = int(index + 1)
    temp_level = int(enemy_level)
    
    # Indeks terakhir monster pemain dicari terlebih dahulu supaya monster dapat ditambahkan setelahnya.
    while monster_inv_db["user_id"][i] <= user:
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

def add_item(user, item, item_inv_db):
    # NB: JIKA AKAN MENGGUNAKAN FUNGSI INI DI DALAM SEBUAH PROSEDUR, TOLONG TULIS from global_var import item_inv_db TERLEBIH DAHULU 
    
    # Pada fungsi ini, akan dilakukan insertion ke database item inventory.
    # Fungsi dibuat seperti di bawah supaya tidak terjadi kesalahan pada fungsi saat mencoba mengakses variabel global.
    # Iterator dan tiga variabel untuk menyetor nilai diinisialisasi terlebih dahulu.
    i = 0
    temp_user = int(user)
    temp_type = str(item)
    temp_quantity = 1
    found = False # Variabel untuk menentukan apakah pemain memiliki item yang dimaksud atau tidak?
    
    # Indeks item pemain dicari terlebih dahulu.
    while item_inv_db["user_id"][i] != user and item_inv_db["user_id"][i] <= user:
        i += 1

    # Setelah ketemu, dicari item yang dimaksud.
    while item_inv_db["user_id"][i] == user and found != True: 
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


def monster_shop_list():
    print(f"{"ID":<2} | {"Monster":<10} | {"ATK":<5} | {"DEF":<5} | {"HP":<5}")
    for i in range(len(monster_db["id"])):
        print(f"{monster_db["id"][i]:<2} | {monster_db["type"][i]:<10} | {monster_db["atk_power"][i]:<5} | {monster_db["def_power"][i]:<5} | {monster_db["hp"][i]:<5}")

def item_shop_list():
    print(f"{"Type":<12} | {"Stock":<4} | {"Price":<4}")
    for i in range(len(item_shop_db["type"])):
        print(f"{item_shop_db["type"][i].capitalize():<12} | {item_shop_db["stock"][i]:<5} | {item_shop_db["price"][i]:<5}")

def monster_shop():
    from global_var import monster_inv_db
    monster_shop_list()
    while True:
        choice = int(input("Ketik ID monster yang ingin kamu beli. (Ketik 'exit' untuk kembali): "))
        if choice == "exit":
            print("Kamu kembali ke menu ...")
            break
        #elif is_numerical(choice) == False:
        #    print("Pilihan bukanlah angka!")
        elif choice > (len(monster_shop_db) + 1) or choice < 1:
            print("ID yang kamu pilih tidak ada!")
        elif currency < monster_shop_db["price"][choice - 1]:
            print("Uang kamu tidak mencukupi untuk membeli monster tersebut!")
        else: 
            print(f"Kamu membeli monster {monster_db["type"][choice-1]}.")
            monster_inv_db = add_monster(user, choice-1, 1, monster_inv_db)


def item_shop():
    from global_var import item_inv_db
    item_shop_list()
    while True:
        choice = input("Ketik nama item yang ingin kamu beli. (Ketik 'exit' untuk kembali): ").lower()
        if choice == "exit":
            print("Kamu kembali ke menu ...")
            break
        elif is_numerical(choice) == True:
            print("Tulis pilihan anda dalam bentuk teks!")
        elif choice != "strength" and choice != "resilience" and choice != "healing" and choice != "monsterball":
            print("Pilihan tidak tersedia!")
        elif currency < item_shop_db["price"][get_idx(choice, item_shop_db["type"])]:
            print("Uang kamu tidak mencukup untuk membeli monster tersebut!")
        else:
            if choice != "monsterball":
                print(f"Kamu membeli potion {choice}.")
            else: 
                print("Kamu membeli monster ball.")    
            item_inv_db = add_item(user, choice, item_inv_db)

def shop():
    print("Selamat datang di Warkom (Warung Komplit) Pak Yanto!")
    while True:
        pilihan = input("Pak Yanto: 'Mau beli apa? (monster/item)' ")
        if pilihan == "monster":
            monster_shop()
            break
        elif pilihan == "item":
            item_shop()
            break
        else: 
            print("Pak Yanto: 'Yang itu mah gak ada, euy!'")

"""

DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.

""" 