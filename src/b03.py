"""
FB03 - Monster Ball
19623296 / Muhammad Ra'if Alkautsar
"""
# As long as it works. T_T

from src.f00 import *
from global_var import *

def monsterball(level: int) -> bool:
    result = rng(0, 20, time.time())
    if level == 1:
        if 0 < result < 15:
            return(True)
        else: 
            return(False)
    elif level == 2:
        if 0 < result < 10:
            return(True)
        else:
            return(False)
    elif level == 3:
        if 0 < result < 5:
            return(True)
        else:
            return(False)
    elif level == 4:
        if 0 < result < 2:
            return(True)
        else:
            return(False)
    else:
        if 0 < result < 1:
            return(True)
        else:
            return(False)

def add_monster(user, index, enemy_level, monster_inv_db):
    # NB: JIKA AKAN MENGGUNAKAN FUNGSI INI DI DALAM SEBUAH PROSEDUR, TOLONG TULIS from global_var import monster_inv_db TERLEBIH DAHULU 

    # Pada fungsi ini, akan dilakukan insertion ke database monster inventory.
    # Fungsi dibuat seperti di bawah supaya tidak terjadi kesalahan pada fungsi saat mencoba mengakses variabel global.

    # Iterator dan tiga variabel untuk menyetor nilai sementara diinisialisasi terlebih dahulu.
    i = 0
    temp_user = int(user)
    temp_index = int(index + 1)
    temp_level = int(enemy_level)
    
    # Indeks terakhir monster pemain dicari terlebih dahulu supaya monster dapat ditambahkan setelahnya.
    while monster_inv_db["user_id"][i] <= user:
        i += 1

    # Setelah ketemu, monster ditambahkan ke indeks setelah indeks terakhir monster pemain.
    # Monster yang tadinya berada di posisi tersebut akan disimpan terlebih dahulu di variabel sementara.
    (monster_inv_db["user_id"][i], temp_user) = (temp_user, monster_inv_db["user_id"][i])
    (monster_inv_db["monster_id"][i], temp_index) = (temp_index, monster_inv_db["monster_id"][i])
    (monster_inv_db["level"][i], temp_level) = (temp_level, monster_inv_db["level"][i])
    i += 1 

    # Setelah itu, kita "mundurkan" semua elemen yang ada setelahnya dengan cara menukar-nukar.
    while i < (len(monster_inv_db["user_id"])):
        
        (monster_inv_db["user_id"][i], temp_user) = (temp_user, monster_inv_db["user_id"][i])
        (monster_inv_db["monster_id"][i], temp_index) = (temp_index, monster_inv_db["monster_id"][i])
        (monster_inv_db["level"][i], temp_level) = (temp_level, monster_inv_db["level"][i])
        i += 1

    # Setelah sampai di indeks terakhir, gunakan append supaya tidak out-of-range.
    monster_inv_db["user_id"].append(temp_user)
    monster_inv_db["monster_id"].append(temp_index)
    monster_inv_db["level"].append(temp_level)
    return(monster_inv_db)


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
"""