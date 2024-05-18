"""
F03 - Logout
19623116 Nayaka
"""

def logout(logged_in: bool):
    if logged_in:
        print("Berhasil logout!")
        return 1
    else: # not logged_in
        print("Logout gagal karena Anda belum login!")


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
