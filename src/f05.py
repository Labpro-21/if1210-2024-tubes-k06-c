"""
F05 - Monster
16523106 Naufal Fakhri Fadhlurrahman
"""

# Kode di sini
from f00 import rng
import sys, os
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(parent_path, 'data')
sys.path.append(parent_path)
sys.path.append(data_path)
# Memuat file .csv yang diperlukan
from global_var import monster_db

def attribute_monster(monster_level: int):
    a = {'atk_power': int(int(monster_db['atk_power'])+[monster_level-1]*0.1)+int(monster_db['atk_power'])}
    a = {'def_power':int(int(monster_db['def_power'])+[monster_level-1]*0.1)+int(monster_db['def_power'])}
    a = {'hp': int(int(monster_db['hp'])+[monster_level-1]*0.1)+int(monster_db['hp'])}
    return a

def atk_power (id: int, monster_level: int):
    b = attribute_monster(monster_level)
    b = int(b[id]['atk_power']) + ((rng(-30,30, 2)/100)*b[id]['atk_power'])

    return b
def atk_result (select_monster, atk_select_monster, defend_monster, def_defend_monster):
    x = atk_power(select_monster,atk_select_monster) * (100-int((monster_db['def_power'])/100))
    if x <0:
        x=0
    return x
print(attribute_monster)


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
Berisi daftar monster yang sudah diteliti oleh Dr. Agus Heisenberg dan dimasukkan
dalam owca-dex. Setiap monster memiliki type, atk power, def power, dan HP

"""