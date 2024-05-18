"""
F14 - Load
19623116 Nayaka
"""

from src.x01 import *
from global_var import *

def read_header(path: str) -> str:
    file = open(path, 'r')
    for line in file:
        return strip_str(line)
    return ""


def load_csv(path: str) -> dict:
    file = open(path, 'r')
    headers = split_str(read_header(path))
    data = {header : [] for header in headers}

    # Menambahkan data pada tiap kolom satu per satu
    for line in file:
        entries = split_str(strip_str(line))
        # Error ketika ada panjang baris yang tidak sama dengan header
        if len(entries) != len(headers):
            raise ValueError("Ada data yang kosong atau melebihi kolom header!")
        # Memproses data csv untuk baris-baris setelah header
        ## Mengambil identitas dari identifier yang ditentukan
        if entries != headers:
            for i in range(len(headers)):
                header, entry = headers[i], entries[i]
                data[header].append(entry)
    file.close()
    return data

def load_data(csv_dir: str):
    user_db = load_csv('data/' + csv_dir + '/user.csv')
    monster_db = load_csv('data/' + csv_dir + '/monster.csv')
    monster_shop_db = load_csv('data/' + csv_dir + '/monster_shop.csv')
    monster_inv_db = load_csv('data/' + csv_dir + '/monster_inventory.csv')
    item_shop_db = load_csv('data/' + csv_dir + '/item_shop.csv')
    item_inv_db = load_csv('data/' + csv_dir + '/item_inventory.csv')

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""
