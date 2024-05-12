"""
F02 - Login
19623116 Nayaka
"""

# Membuka path ke folder 'data'
import sys, os
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(parent_path, 'data')
sys.path.append(parent_path)
sys.path.append(data_path)
# Memuat database yang sudah disimpan di dictionary `user_db` dalam module global_var
from global_var import *


# FUNGSI login()
def login(db: dict = user_db):
    # Ra'if ini ntar tolong dicakepin yah itunya
    print("<=============>")
    print("  O. W. C. A.  ")
    print("   We serve.   ")
    print("<=============>")

    # Bagian utama fungsi
    username = input_username(db)
    input_password(username, db)

# FUNGSI input_username()
def input_username(db: dict = user_db):
    valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    username = input("Username: ")
    remove_nth_line(1)
    valid1 = subset(username, valid_char)
    valid2 = is_in(username, db["username"])

    while not valid1 or not valid2:
        if not valid1:
            print("Username hanya boleh berisi alfabet, angka, tanda hubung bawah (_), dan tanda strip (-)!")
        else: # not valid2
            print("Username tidak terdaftar. ")
        username = input("Username: ")
        remove_nth_line(1)
        valid1 = subset(username, valid_char)
        valid2 = is_in(username, db["username"])
        remove_nth_line(1)
    return username

# FUNGSI input_password()
def input_password(username: str, db: dict = user_db):
    user_idx = get_idx(username, db["username"])

    password = input("Password: ")
    remove_nth_line(1)
    valid = db["password"][user_idx] == password
    if valid:
            return password
    else:
        while not valid:
            print("Password salah!")
            password = input("Password: ")
            remove_nth_line(1)
            valid = db["password"][user_idx] == password
            remove_nth_line(1)
    
"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
Fungsi login() akan menerima username dan password dari pengguna dan mengecek validitasnya.
Fungsi akan terus menerima input hingga username atau password sesuai. Selanjutnya, variabel
logged_in pada global_var.py akan diubah nilainya menjadi True, mengindikasikan pengguna telah
berhasil login ke dalam program.

"""