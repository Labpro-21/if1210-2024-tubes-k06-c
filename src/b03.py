"""
FB03 - Monster Ball
NIM NAMA
"""
from f00 import *

def monsterball():
    global enemyMonster
    result = rng(0, 20, time.time())
    if enemyMonster["lv"] == 1:
        if 0 < result < 15:
            print("Selamat, monster berhasil tertangkap!")
            monsterCaught()
            isBattle = False
        else: 
            print("Monster lepas!")
    elif enemyMonster["lv"] == 2:
        if 0 < result < 10:
            print("Monster berhasil tertangkap!")
            monsterCaught()
            isBattle = False
        else:
            print("Monster lepas!")
    elif enemyMonster["lv"] == 3:
        if 0 < result < 5:
            print("Monster berhasil tertangkap!")
            monsterCaught()
            isBattle = False
        else:
            print("Monster lepas!")
    elif enemyMonster["lv"] == 4:
        if 0 < result < 2:
            print("Monster berhasil tertangkap!")
            monsterCaught()
            isBattle = False
        else:
            print("Monster lepas!")
    else:
        if 0 < result < 1:
            print()
            monsterCaught()
            isBattle = False
        else:
            print("Monster lepas!")

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""