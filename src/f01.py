"""
F01 - Register
19623116 Nayaka
"""

# Membuka database yang sudah di-load dan disimpan di global_var
from global_var import *

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
    user_db["id"].append(last(user_db["id"]) + 1)
    user_db["username"].append(username)
    user_db["password"].append(password)
    user_db["role"].append('agent')
    user_db["oc"].append(0)

# FUNGSI input_username_reg()
def input_username_reg():
    valid_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    username = input("Username: ")

    valid = subset(username, valid_char)
    while not valid:
        remove_nth_line(1)
        print("Username hanya boleh berisi alfabet, angka, tanda hubung bawah (_), dan tanda strip (-)!")
        username = input("Username: ")
        remove_nth_line(1)
        valid = subset(username, valid_char)
        if valid:
            remove_nth_line(1)
    return username

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
Fungsi register() akan mendaftarkan akun baru untuk agent dengan username dan password
sesuai dengan yang diinput oleh pengguna. Fungsi input_username_reg() digunakan untuk
menerima username dari akun yang akan dibuat dan memvalidasinya. 

Di sini global_var dimuat agar kita dapat mengakses database username dari user.csv yang sudah di-load.
Perhatikan bahwa remove_nth_line() yang merupakan fungsi dari x01 dapat digunakan tanpa
memuat x01.py secara eksplisit karena sudah dimuat lewat f14 dari global_var.
"""