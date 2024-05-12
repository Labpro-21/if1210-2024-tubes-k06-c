"""
F05 - Monster
16523106 Naufal Fakhri Fadhlurrahman
"""

# Kode di sini

from f00 import *
from x01 import *
import sys, os
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(parent_path, 'data')
sys.path.append(parent_path)
sys.path.append(data_path)
# Memuat file .csv yang diperlukan
from global_var import *
def attribute_monster(id: int, monster_level: int, monster_db):
    monster = monster_db['id'].index(id)
    monster_db['atk_power'][monster] = int(monster_db['atk_power'][monster] + (monster_level - 1) * 0.1 * monster_db['atk_power'][monster])
    monster_db['def_power'][monster] = int(monster_db['def_power'][monster] + (monster_level - 1) * 0.1 * monster_db['def_power'][monster])
    monster_db['hp'][monster] = int(monster_db['hp'][monster] + (monster_level - 1) * 0.1 * monster_db['hp'][monster])
    return monster_db
print(attribute_monster(3,2,monster_db))
def atk_power(id: int, monster_db):
    monster_index = monster_db['id'].index(id)
    atk = int(monster_db['atk_power'][monster_index] + ((rng(-30, 30, 2 ) / 100) * monster_db['atk_power'][monster_index]))
    return atk


def atk_result(attacker_id: int, defender_id: int, monster_db):
    attacker_index = monster_db['id'].index(attacker_id)
    defender_index = monster_db['id'].index(defender_id)
    
    attacker_atk = atk_power(attacker_id, monster_db)
    defender_def = monster_db['def_power'][defender_index]
    
    damage = attacker_atk * (1 - int(defender_def) / 100)
    
    if damage < 0:
        damage = 0
    
    return damage



"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
Berisi daftar monster yang sudah diteliti oleh Dr. Agus Heisenberg dan dimasukkan
dalam owca-dex. Setiap monster memiliki type, atk power, def power, dan HP

"""