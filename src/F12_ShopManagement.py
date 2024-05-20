"""
F12 - Shop Management
19623296 Muhammad Ra'if Alkautsar
"""

# type;stock;price
# strength;10;50
# resilience;5;30
# healing;3;20
# monsterball;5;50

from src.x01 import *
from src.F10_ShopCurrency import *
from src.F05_Monster import *

def input_validation(masukan, validation, error_message):
    while True:
        value = input(masukan)
        if validation(value):
            return value
        else:
            print(error_message)

def add_monster_shop(monster_shop_db, monster_id, stock, price):
    if monster_id not in monster_shop_db["monster_id"]:
        monster_shop_db["monster_id"].append(monster_id)
        monster_shop_db["stock"].append(stock)
        monster_shop_db["price"].append(price)
        print("Monster ditambahkan ke shop")
    else:
        print("Monster sudah ada di shop!")
    return(monster_shop_db)

def remove_monster_shop(monster_shop_db, monster_id):
    if monster_id in monster_shop_db['monster_id']:
        idx = get_idx(monster_shop_db['monster_id'], monster_id)
        monster_db["id"] = remove_ele(idx, monster_db["monster_id"])
        monster_db["type"] = remove_ele(idx, monster_db["stock"])
        monster_db["atk_power"] = remove_ele(idx, monster_db["price"])
        print("Monster dihapus dari shop.")
    else:
        print("ID monster tidak ditemukan!")
    return(monster_shop_db)

def change_monster_shop(monster_shop_db, monster_id, stock, price):
    if monster_id in monster_shop_db['monster_id']:
        idx = get_idx(monster_shop_db['monster_id'])
        monster_shop_db['stock'][idx] = stock
        monster_shop_db['price'][idx] = price
        print("Data di shop berhasil diubah.")
    else:
        print("ID monster tidak ditemukan!")

def add_item_shop(item_shop_db, item_type, stock, price):
    item_shop_db['type'].append(item_type)
    item_shop_db['stock'].append(stock)
    item_shop_db['price'].append(price)
    print(f"{item_type.capitalize()} berhasil ditambahkan.")
    return(item_shop_db)

def remove_item_shop(item_shop_db, item_type):
    if item_type in item_shop_db['type']:
        index = item_shop_db['type'].index(item_type)
        for key in item_shop_db.keys():
            del item_shop_db[key][index]
        print("Item dihapus dari toko.")
    else:
        print("Item tidak ditemukan.")
    return(item_shop_db)

def change_item_shop(item_shop_db, item_type, price):
    if item_type in monster_shop_db['monster_id']:
        idx = get_idx(item_shop_db["type"][item_type])
        item_shop_db['stock'][idx] = stock
        item_shop_db['price'][idx] = price
        print("Data di shop berhasil diubah.")
    else:
        print("Item tidak ditemukan!")
    return(item_shop_db)

def item_shop_management(item_shop_db):
    item_shop_list(item_shop_db)
    print("Mau tambah, hapus, atau ubah item di shop?")
    while True:
        choice = str(input("Ketik 'tambah' untuk menambahkan item, 'hapus' untuk menghapus item, 'ubah' untuk mengubah item, dan 'exit' untuk keluar.").lower())
        if is_numerical(choice):
            print("Input harus berupa teks!")
        else:
            if choice == "tambah":
                item_type = input_validation("Masukkan tipe item: ", is_string, "Tipe harus berupa teks!")
                stock = input_validation("Masukkan stock item: ", is_numerical, "Stock harus berupa angka!")
                price = input_validation("Masukkan harga item: ", is_numerical, "Harga harus berupa angka!")
                item_shop_db = add_item_shop(item_shop_db, item_type, stock, price)
            elif choice == "hapus":
                item_type = input_validation("Masukkan tipe item yang ingin dihapus: ", is_string, "Tipe item harus berupa teks!")
                item_shop_db = remove_item_shop(item_shop_db, item_type)
            elif choice == "ubah":
                item_type = input_validation("Masukkan tipe item yang ingin diubah: ", is_string, "Tipe item harus berupa teks!")
                stock = input_validation("Masukkan stock item baru: ", is_numerical, "Stock item harus berupa angka!")
                price = input_validation("Masukkan harga item baru: ", is_numerical, "Harga item harus berupa angka!")
                item_shop_db = change_item_shop(item_shop_db, item_type, stock, price)
            elif choice == "exit":
                break
            else:
                print("Input tidak valid!")
    return(item_shop_db)

def monster_shop_management(monster_db, monster_shop_db):
    monster_shop_list(monster_shop_db, monster_db)
    print("Mau tambah, hapus, atau ubah monster di shop?")
    while True:
        choice = str(input("Ketik 'tambah' untuk menambahkan monster, 'hapus' untuk menghapus monster, 'ubah' untuk mengubah monster, dan 'exit' untuk keluar.").lower())
        if is_numerical(choice):
            print("Input harus berupa teks!")
        else:
            if choice == "tambah":
                monster_id = input_validation("Masukkan ID monster: ", is_numerical, "ID monster harus berupa angka!")
                stock = input_validation("Masukkan stock monster: ", is_numerical, "Stock monster harus berupa angka!")
                price = input_validation("Masukkan harga monster: ", is_numerical, "Harga monster harus berupa angka!")
                monster_shop_db = add_monster_shop(monster_shop_db, monster_id, stock, price)
            elif choice == "hapus":
                monster_id = input_validation("Masukkan ID monster yang ingin dihapus: ", is_numerical, "ID monster harus berupa angka!")
                monster_shop_db = remove_monster_shop(monster_shop_db, monster_id)
            elif choice == "ubah":
                monster_id = input_validation("Masukkan ID monster yang ingin diubah: ", is_numerical, "ID monster harus berupa angka!")
                stock = input_validation("Masukkan stock monster baru: ", is_numerical, "Stock monster harus berupa angka!")
                price = input_validation("Masukkan harga monster baru: ", is_numerical, "Harga monster harus berupa angka!")
                monster_shop_db = change_monster_shop(monster_shop_db, monster_id, stock, price)
            elif choice == "exit":
                break
            else:
                print("Input tidak valid!")
    return(monster_shop_db)

def shop_management(monster_shop_db, item_shop_db):
    print("Selamat datang di shop management!")
    print("Mau edit database monster atau shop?")
    while True:
        choice = str(input("Ketik 'monster' untuk mengelola monster, 'item' untuk mengelola item, dan 'exit' untuk keluar.").lower())
        if is_numerical(choice):
            print("Input harus berupa teks!")
        else:
            if choice == "monster":
                monster_shop_management(monster_db, monster_shop_db)
            elif choice == "item":
                item_shop_management(item_shop_db)
            elif choice == "exit":
                break
            else:
                print("Input tidak valid!")
"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
