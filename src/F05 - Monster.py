"""
F05 - Monster
16523106 Naufal Fakhri Fadhlurrahman
19623296 Muhammad Ra'if Alkautsar
"""

# Kode di sini

from src.f00 import *
from src.x01 import *
import sys, os
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(parent_path, 'data')
sys.path.append(parent_path)
sys.path.append(data_path)

# Memuat file .csv yang diperlukan
from global_var import *
def attribute_monster(id: int, monster_level: int, monster_db): 
    monster = monster_db['id'].index(id)
    monster_type = monster_db['type'][monster]
    monster_atk = int(monster_db['atk_power'][monster] + (monster_level - 1) * 0.1 * monster_db['atk_power'][monster])
    monster_def = int(monster_db['def_power'][monster] + (monster_level - 1) * 0.1 * monster_db['def_power'][monster])
    monster_hp = int(monster_db['hp'][monster] + (monster_level - 1) * 0.1 * monster_db['hp'][monster])
    return (monster_type, monster_atk, monster_def, monster_hp)

def atk_power(atk_value):
    atk = int(atk_value + ((rng(-30, 30, 2 ) / 100) * atk_value))
    return atk

def atk_result(attacker_atk_value, defender_def_value):
    attacker_atk = atk_power(attacker_atk_value)
    damage = attacker_atk * (1 - int(defender_def_value) / 100)
    print(f"ATK Value: {attacker_atk_value}. DEF Value: {defender_def_value}.")
    
    if damage < 0:
        damage = 0
    
    return damage

""" def atk_power(id: int, monster_db):
    monster_index = monster_db['id'].index(id)
    atk = int(monster_db['atk_power'][monster_index] + ((rng(-30, 30, 2 ) / 100) * monster_db['atk_power'][monster_index]))
    return atk """

""" def atk_result(attacker_id: int, defender_id: int, monster_attacker, monster_defender):
    attacker_index = monster_attacker['id'].index(attacker_id)
    defender_index = monster_defender['id'].index(defender_id)
    
    attacker_atk = atk_power(attacker_id, monster_attacker)
    defender_def = monster_defender['def_power'][defender_index]
    
    damage = attacker_atk * (1 - int(defender_def) / 100)
    
    if damage < 0:
        damage = 0
    
    return damage
 """


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
Berisi daftar monster yang sudah diteliti oleh Dr. Agus Heisenberg dan dimasukkan
dalam owca-dex. Setiap monster memiliki type, atk power, def power, dan HP

"""
