"""
F03 - Logout
19623116 Nayaka
"""

from src.global_var import *

def logout(logged_in: bool):
    if logged_in:
        print("Berhasil logout!")
<<<<<<< Updated upstream
        return 1
=======
        logged_in = False
>>>>>>> Stashed changes
    else: # not logged_in
        print("Logout gagal karena Anda belum login!")


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
