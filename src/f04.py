"""
F04 - Menu & Help
NIM NAMA
"""
from src.x01 import *

user = csv_parser("data/user.csv")
username = input()
id = user[username][id]

# Kode di sini
def help(id):
    if userid == 0:
        print("=========== HELP ===========")
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print("   1. Login: Masuk ke dalam akun yang sudah terdaftar.")
        print("   2. Register: Membuat akun baru.")
        print("                                                                               ")
        print("Footnote:")
        print("   1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.")
        print("   2. Jangan lupa untuk memasukkan input yang valid.")
    else: # id != 0 

        if role == "admin":
            print("=========== HELP ===========")
            print("Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan.")
            print("   1. Logout            : Keluar dari akun yang sedang digunakan.")
            print("   2. Shop              : Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent.")
            print("   3. Monster Management: Menambahkan monster baru ke dalam database.") 
            print("                                                                               ")                                                                                                                                                          ")
            print("Footnote:")
            print("   1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.")
            print("   2. Jangan lupa untuk memasukkan input yang valid.")
        elif role == agent :
            if role == agnet   then:
            print("=========== HELP ===========")
            print(f"Selamat datang {username}. Berikut adalah hal-hal yang dapat kamu lakukan.")
            print("   1. Logout    : Keluar dari akun yang sedang digunakan.")
            print("   2. Shop      : Membeli agent, monster dan potion.")
            print("   3. Inventory : Menampilkan monster dan potion serta spesifikasi yang dimiliki .")    
            print("   4. Battle    : Melakukan pertarungan melawan monster.") 
            print("   5. Arena     : Melatih monster dan mendapat koin oc saat menang .") 
            print("   6. Laboratory: Mengupgrade monster yang ada di invetory dengan koin oc.") 
            print("                                                                               ")                                                                                                                                                ")
            print("Footnote:")
            print("   1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.")
            print("   2. Jangan lupa untuk memasukkan input yang valid.")
        else: 
            print("ok")
        

"""""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
