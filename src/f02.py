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
# Memuat file .csv yang diperlukan
from global_var import *

# FUNGSI input_username()
def input_username():
    global user_db
    valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    username = input("Username: ")
    remove_nth_line(1)
    valid1 = subset(username, valid_char)
    valid2 = is_in(username, user_db["username"])


    while not valid1 or not valid2:
        if not valid1:
            print("Username hanya boleh berisi alfabet, angka, tanda hubung bawah (_), dan tanda strip (-)!")
        elif not valid2:
            print("Username tidak terdaftar. ")
        username = input("Username: ")
        remove_nth_line(1)
        valid1 = subset(username, valid_char)
        valid2 = is_in(username, user_db["username"])
        remove_nth_line(1)
    return username

# FUNGSI input_password()
def input_password(username: str):
    global user_db
    user_idx = get_idx(username, user_db["username"])

    password = input("Password: ")
    remove_nth_line(1)
    valid = user_db["password"][user_idx] == password
    if valid:
            return password
    else:
        while not valid:
            print("Password salah!")
            password = input("Password: ")
            remove_nth_line(1)
            valid = user_db["password"][user_idx] == password
            remove_nth_line(1)
    
# FUNGSI login()
def login():

    # Ra'if ini ntar tolong dicakepin yah itunya
    print("<=============>")
    print("  O. W. C. A.  ")
    print("   We serve.   ")
    print("<=============>")

    # Bagian utama fungsi
    username = input_username()
    password = input_password(username)

login()
    

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""