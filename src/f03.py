"""
F03 - Logout
19623116 Nayaka
"""

from global_var import *

def logout(logged_in: bool) -> int:
    if logged_in:
        print("Berhasil logout!")
        logged_in = False
        return 1
    else: # not logged_in
        print("Logout gagal karena Anda belum login!")
    return 0


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""