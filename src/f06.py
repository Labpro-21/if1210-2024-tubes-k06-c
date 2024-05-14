"""
F06 - Potion
16523106 Naufal Fakhri Fadhlurrahman
"""

# Kode di sini
from src.f05 import *
import sys, os
parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_path = os.path.join(parent_path, 'data')
sys.path.append(parent_path)
sys.path.append(data_path)
# Memuat file .csv yang diperlukan
from global_var import *

def strength_potion(atk_power: int):
    increase = int(atk_power * 0.05)
    return atk_power + increase

def resilience_potion(def_power: int):
    increase = int(def_power * 0.05)
    return def_power + increase

def healing_potion(current_hp: int, max_hp: int):
    heal_amount = int(max_hp * 0.25)
    new_hp = current_hp + heal_amount
    return min(new_hp, max_hp)  # Make sure HP doesn't exceed max HP


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""