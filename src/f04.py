"""
F04 - Menu & Help
16523146 Sacca Kovida Kasmaji
"""
from global_var import *
# Contoh dan belum dismabungkan dengan login
current_user = get_idx("Asep_Spakbor",user_db["username"])

# Kode di sini
def help(username):
    if user_db["role"][current_user] == "admin":
        print("""
============================================ HELP ============================================
                                                                                
Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan.
                                                                                
    1. Logout            : Keluar dari akun yang sedang digunakan.
    2. Shop              : Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent.
    3. Monster Management: Menambahkan monster baru ke dalam database. 

Footnote:
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.
    2. Jangan lupa untuk memasukkan input yang valid.
        """)
    elif user_db["role"][current_user] == "agent":
        print(f"""
============================================ HELP ============================================
                                                                                    
Halo Agent {user_db["username"][current_user]}.Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu 
tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang: 
                                                                                
    1. Logout    : Keluar dari akun yang sedang digunakan.
    2. Shop      : Membeli agent, monster dan potion.
    3. Inventory : Menampilkan monster dan potion serta spesifikasi yang dimiliki .    
    4. Battle    : Melakukan pertarungan melawan monster. 
    5. Arena     : Melatih monster dan mendapat koin oc saat menang . 
    6. Laboratory: Mengupgrade monster yang ada di invetory dengan koin oc. 
                                                                                
Footnote:
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.
    2. Jangan lupa untuk memasukkan input yang valid.
        """)  
    else: # belum login
        print("""
============================================ HELP ============================================
                                                                                
Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.
                                                                                
    1. Login: Masuk ke dalam akun yang sudah terdaftar.
    2. Register: Membuat akun baru.
                                                                                
Footnote:
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar.
    2. Jangan lupa untuk memasukkan input yang valid.
        """)

help(current_user)
"""""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
