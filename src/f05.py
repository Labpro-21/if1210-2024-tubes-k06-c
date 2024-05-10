"""
F05 - Monster
16523106 Naufal Fakhri Fadhlurrahman
"""

# Kode di sini
from f00 import rng
from x01 import csv_parser
csv_parser('C:\\Users\\Lenovo\\OneDrive - Institut Teknologi Bandung\Documents\\if1210-2024-tubes-k06-c\\data\\monster.csv')

def attribute_monster (monster_id: int, monster_level: int):
    a = csv_parser('C:\\Users\\Lenovo\\OneDrive - Institut Teknologi Bandung\\Documents\\if1210-2024-tubes-k06-c\\data\\monster.csv')
    a[monster_id-1]['atk_power'] = int(int(a[monster_id-1]['atk_power']))+(((monster_level-1)* 0.1)*int(a[monster_id-1]['atk_power']))
    a[monster_id-1]['def_power'] = int(int(a[monster_id-1]['def_power']))+(((monster_level-1)* 0.1)*int(a[monster_id-1]['def_power']))
    a[monster_id-1]['hp'] = int(int(a[monster_id-1]['hp']))+(((monster_level-1)* 0.1)*int(a[monster_id-1]['hp']))

    return a
def atk_power (monster_id: int, monster_level: int):
    b = attribute_monster(monster_id, monster_level)
    b = int(b[monster_id]['atk_power']) + ((rng(-30,30, 2)/100)*b[monster_id]['atk_power'])

    return b
def atk_result (select_monster, atk_select_monster, defend_monster, def_defend_monster):
    select = attribute_monster(select_monster, atk_select_monster)
    defending = attribute_monster(defend_monster, def_defend_monster)
    x = atk_power(select_monster,atk_select_monster) * (100-int(defending[defend_monster]['def_defend_monster'])/100)
    if x <0:
        x=0
    return x




   
"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
Berisi daftar monster yang sudah diteliti oleh Dr. Agus Heisenberg dan dimasukkan
dalam owca-dex. Setiap monster memiliki type, atk power, def power, dan HP

"""