"""
TUGAS BESAR IF1210 DASAR PEMROGRAMAN
K06-C

19623116    Zulfaqqar Nayaka Athadiansyah	
19623296    Muhammad Ra'if Alkautsar
19623076    Daniel A. M. Sipayung
16523106    Naufal Fakhri Fadhlurrahman
16523146    Sacca Kovida Kasmaji

SEKOLAH TEKNIK ELEKTRO DAN INFORMATIKA
INSTITUT TEKNOLOGI BANDUNG
2024
"""

# Mengimpor library yang dibutuhkan
from nt import error
import os, argparse

# Mengimpor fungsi-fungsi yang sudah dibuat dengan penuh jerih payah
from src.x01 import *
from src.F01_Register import *
from src.F02_Login import *
from src.F03_Logout import *
from src.F15_Save import *
from src.F16_Exit import *
from src.F03_Logout import *
from src.F04_MenuHelp import *
# from src.F07_Inventory import *
from src.B05_PetaKotaDanville import *
from src.F12_ShopManagement import *
from src.F08_Battle import *
from src.F09_Arena import *
from src.F11_Laboratory import *
from src.F13_MonsterManagement import *
from src.B04_JACKPOT import *
from global_var import *

# argparse
parser = argparse.ArgumentParser(description="Menjalankan program dan memuat database csv")
parser.add_argument("dir", help="Direktori penyimpanan database CSV", nargs='?')
args = parser.parse_args()

if args.dir is None:
    os.system('cls')
    print("Tidak ada nama folder yang diberikan!")
    print("Penggunaan: python main.py <nama_folder>")
    sys.exit(1)
else:
    os.system('cls')
    csv_dir = str(args.dir)
    while not validate_dir("data/" + csv_dir):
        if validate_dir("data/" + csv_dir):
            break
        else:
            print(f"Folder {csv_dir} tidak ditemukan! Mohon masukkan nama folder yang valid dalam direktori 'data'.")
            sys.exit(1)
    database        = load_data(csv_dir)
    user_db         = database[0]
    monster_db      = database[1]
    monster_shop_db = database[2]
    monster_inv_db  = database[3]
    item_shop_db    = database[4]
    item_inv_db     = database[5]


# Loading Screen
print("Mohon maximize window command prompt Anda untuk pengalaman terbaik.")
time.sleep(3)
for i in range(5):
    remove_nth_line(1)
    print(f"Memulai program dalam {5-i} detik...")
    time.sleep(1)
remove_nth_line(1)
print("Selesai!")
time.sleep(2)
remove_nth_line(1)
remove_nth_line(1)

def title_screen():
    username = ""
    logged_in = False
    while True:
        print_text("data/title_screen.txt") 
        action = input(">>> ")
        remove_nth_line(1)
        match lower(action):
            case "login":
                # os.system('cls')
                username = login(user_db)
                logged_in = True
                print("Berhasil login!")
                if user_db["role"][get_idx(username, user_db["username"])] == "admin":
                    admin_gameplay(user_db, monster_db, monster_shop_db, item_shop_db)
                else:
                    main_gameplay(username, user_db, monster_db, monster_shop_db, monster_inv_db, item_shop_db, item_inv_db)
            case "register":
                # os.system('cls')
                register(user_db)
                print("Berhasil register!")
            case "menu":
                menu(username, logged_in, user_db)
            case "save":
                # os.system('cls')
                save_dir = input("Folder savegame: ")
                if not validate_dir('data/' + save_dir):
                    os.makedirs('data/' + save_dir)
                save(user_db, 'data/' + save_dir + '/user.csv')
                print("Berhasil menyimpan!")
            case "exit":
                # os.system('cls')
                exit(csv_dir)
                break
            case _:
                continue

## BEDAKAN user_id, user_idx, DAN username!!
## user_id adalah id dari user di database (mulai dari 1)!
## user_idx adalah index dari user di database (mulai dari 0 atau user_id - 1)!
## username adalah username dari user yang sedang login!

def main_gameplay(username, user_db, monster_db, monster_shop_db, monster_inv_db, item_shop_db, item_inv_db):
    print("Selamat berpetualang!")
    print("Ketik 'help' untuk menerima bantuan.")
    user_idx = get_idx(username, user_db["username"])
    user_id = user_db["id"][user_idx]
    posx, posy = user_db["posx"][user_idx], user_db["posy"][user_idx]
    worldmap = read_map(10, 10, "data/map.txt", posx, posy)
    oc = user_db["oc"][user_idx]
    while True:
        print_map(worldmap, 10, 10)
        action = input(">>> ")
        remove_nth_line(1)
        if action == "up" or action == "u":
            worldmap, posx, posy = moveUp(worldmap, posx, posy)
        elif action == "right" or action == "r":
            worldmap, posx, posy = moveRight(worldmap, posx, posy)
        elif action == "left" or action == "l":
            worldmap, posx, posy = moveLeft(worldmap, posx, posy)
        elif action == "down" or action == "d":
            worldmap, posx, posy = moveDown(worldmap, posx, posy)
        elif action == "inventory":
            show_inventory(item_inv_db, monster_inv_db, monster_db, user_id)
        elif action == "logout":
            print("Berhasil logout!")
            title_screen()
            break
        elif action == "save":
            save(user_db, 'data/' + csv_dir + '/user.csv')
            print("Berhasil menyimpan!")
        elif action == "help":
            menu("agent")
        elif action == "exit":
            exit(csv_dir)
            break
        elif action == "shop":
            if checkProximity(action, posx, posy, worldmap):
                monster_inv_db, item_inv_db, monster_shop_db, item_shop_db, oc = shop(monster_inv_db, item_inv_db, monster_shop_db, item_shop_db, monster_db, oc, user_id)
        elif action == "battle":
            if checkProximity(action, posx, posy, worldmap):
                monster_inv_db, item_inv_db, damage_dealt, damage_received = battle(monster_db, monster_inv_db, user_idx, rng(0, 5, time.time()), item_inv_db, oc, "wild")
        elif action == "laboratory":
            if checkProximity(action, posx, posy, worldmap):
                monster_inv_db, oc = laboratory(user_id, monster_db, monster_inv_db, oc)
        elif action == "arena":
            if checkProximity(action, posx, posy, worldmap):
                arena(monster_db, monster_inv_db, user_id, item_inv_db, oc)
        elif action == "jackpot":
            if checkProximity(action, posx, posy, worldmap):
                oc, monster_inv_db = jackpot(oc, user_id, monster_db, monster_inv_db)
        elif action == "debug":
            print("Username:", username) 
            print("user_db:", user_db)
            print("monster_db:", monster_db) 
            print("monster_shop_db:", monster_shop_db) 
            print("monster_inv_db:", monster_inv_db)
            print("item_shop_db:", item_shop_db)
            print("item_inv_db:", item_inv_db)
            print("OC:", oc)
        else: 
            print("Pergerakan tidak valid!")    

def admin_gameplay(user_db, monster_db, monster_shop_db, item_shop_db):
    print("Selamat datang di kursi admin! ('Kursi ini sangat empuk!', pikirmu.)")
    print("Pilihan opsi: monster (untuk monster management), shop (untuk shop management), logout, save, help, dan exit.")
    while True:
        action = str(input(">>>"))
        remove_nth_line(1)
        if action == "monster":
            monster_management(monster_db)
        elif action == "shop":
            shop_management(monster_shop_db, item_shop_db)
        elif action == "logout":
            print("Berhasil logout!")
            title_screen()
            break
        elif action == "save":
            save(user_db, 'data/' + csv_dir + '/user.csv')
            print("Berhasil menyimpan!")
        elif action == "help":
            menu("admin")
        elif action == "exit":
            exit(csv_dir)
        elif action == "debug":
            print("user_db:", user_db)
            print("monster_db:", monster_db) 
            print("monster_shop_db:", monster_shop_db) 
            print("item_shop_db:", item_shop_db)
        else:
            print("Pilihan tidak valid!")

title_screen()