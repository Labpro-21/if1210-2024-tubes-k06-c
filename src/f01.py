"""
F01 - Register
19623116 Nayaka
"""

# Membuka path ke folder 'data'
import sys, os
data_path = os.path.join(os.path.dirname(__file__), 'data')
sys.path.append(data_path)

# Memuat file .csv yang diperlukan
from x02 import *
user_db = csv_parser("data/user.csv", "username")
monster_db = csv_parser("data/monster.csv", "type")

# FUNGSI input_username()
def input_username():
    global user_db
    valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    username = input("Username: ")

    valid1 = subset(username, valid_char)
    valid2 = is_in(username, )
    while not valid1:
        remove_nth_line(1)
        print("Username hanya boleh berisi alfabet, angka, tanda hubung bawah (_), dan tanda strip (-)!")
        username = input("Username: ")
        remove_nth_line(1)
        valid1 = subset(username, valid_char)
        if valid1:
            remove_nth_line(1)
    return username

# FUNGSI input_password()
def input_password(username: str):
    global user_db
    password = input("Password: ")
    if user_db["password"][username] == password:
            return password
    else:
        while user_db["password"][username] != password:
            print("negro!")
            password = input("Password: ")

# FUNGSI register()
def register():

    # Ra'if ini ntar tolong dicakepin yah itunya
    print("<=============>")
    print("  O. W. C. A.  ")
    print("   We serve.   ")
    print("<=============>")

    # Bagian utama fungsi
    username = input_username()
    password = input_password(username)
    
    
register()

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""