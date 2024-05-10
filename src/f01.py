"""
F01 - Register
19623116 Nayaka
"""

# Membuka path ke folder 'data'
import sys, os
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(parent_path, 'data')
sys.path.append(parent_path)
sys.path.append(data_path)
# Memuat file .csv yang diperlukan
from global_var import *

# FUNGSI input_username()
def input_username_reg():
    global user_db
    valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    username = input("Username: ")

    valid1 = subset(username, valid_char)
    while not valid1:
        remove_nth_line(1)
        print("Username hanya boleh berisi alfabet, angka, tanda hubung bawah (_), dan tanda strip (-)!")
        username = input("Username: ")
        remove_nth_line(1)
        valid1 = subset(username, valid_char)
        if valid1:
            remove_nth_line(1)
    
    valid2 = not is_in(username, user_db["username"])
    while not valid2:
        remove_nth_line(1)
        print("Username sudah terdaftar. ")
        username = input("Username: ")
        valid2 = not is_in(username, user_db["username"])
        remove_nth_line(1)
        if valid2:
            remove_nth_line(1)
    return username

# FUNGSI register()
def register():
    # Ra'if ini ntar tolong dicakepin yah itunya
    print("<=============>")
    print("  O. W. C. A.  ")
    print("   We serve.   ")
    print("<=============>")

    # Bagian utama fungsi
    username = input_username_reg()
    password = input("Password: ")

    # Menambahkan data pengguna ke dalam database
    user_db["username"].append(username)
    user_db["password"].append(password)
    user_db["role"].append('agent')
    user_db["oc"].append(0)

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""