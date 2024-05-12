"""
F16 - Exit
19623116 Nayaka
"""
from src.f15 import *
from src.x01 import *
from global_var import *

def exit():
    global user_db, a, monster_shop_db, monster_inv_db, item_shop_db, item_inv_db
    save_prompt = input("Apakah Anda ingin menyimpan progres Anda? (y/n)")
    if save_prompt == "Y" or "y":
        print("Menyimpan database ke dalam csv... [user.csv]")
        save(user_db, "data/user.csv")
        print("Menyimpan database ke dalam csv... [monster.csv]")
        save(a, "data/monster.csv")
        print("Menyimpan database ke dalam csv... [monster_shop.csv]")
        save(monster_shop_db, "data/monster_shop.csv")
        print("Menyimpan database ke dalam csv... [monster_inventory.csv]")
        save(monster_inv_db, "data/monster_inventory.csv")
        print("Menyimpan database ke dalam csv... [item_shop.csv]")
        save(item_shop_db, "data/item_shop.csv")
        print("Menyimpan database ke dalam csv... [item_inventory.csv]")
        save(item_inv_db, "data/item_inventory.csv")
        print("Proses penyimpanan selesai.")
        time.sleep(1)
        print("Sampai jumpa di lain waktu :D")
    elif save_prompt == "N" or "n":
        print("Sampai jumpa di lain waktu :D")
    else:
        remove_nth_line(1)
        exit()

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
Ketika pengguna ingin keluar dari program, pengguna diberi pilihan untuk menyimpan
progresnya atau tidak. Jika pengguna berkenan, seluruh database dalam program yang
tersimpan dalam bentuk dictionary akan di-parsing ulang menjadi baris-baris yang dipisahkan
dengan semikolon (;) lalu file .csv tujuan akan ditimpa baris per baris dengan data yang baru.
Jika input yang diterima (terkait kesediaan pengguna untuk menyimpan data) tidak valid, yakni selain Y/N
(case insensitive), pengguna terus diminta untuk memberikan input hingga valid.

"""