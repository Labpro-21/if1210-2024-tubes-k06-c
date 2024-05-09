"""
X01 - Fungsi-fungsi Pembantu 2
19623116 Nayaka
"""
import os, sys
# Mengimpor fungsi-fungsi yang sudah dibuat dengan penuh jerih payah
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

from x01 import *
# Jika ingin menjalankan file ini secara independen
# (bukan sebagai module dari main.py) hilangkan "src."

def read_header(path: str) -> str:
    file = open(path, 'r')
    for line in file:
        return line.strip()

def csv_parser(path: str, identifier: str) -> list[dict]:
    file = open(path, 'r')
    headers = split_str(read_header(path))
    data = {header : {} for header in headers}
    
    # Mencari indeks dari identifier
    identifier_idx = -1
    for i in range(len(headers)):
        if headers[i] == identifier:
            identifier_idx = i
    if identifier_idx == -1:
        raise ValueError("Identifier tidak ditemukan!")

    # Menambahkan data pada tiap kolom satu per satu
    for line in file:
        entries = split_str(strip_str(line))
        # Error ketika ada panjang baris yang tidak sama dengan header
        if len(entries) != len(headers):
            raise ValueError("Ada data yang kosong atau melebihi kolom header!")
        # Memproses data csv untuk baris-baris setelah header
        ## Mengambil identitas dari identifier yang ditentukan
        if entries != headers:
            identifier_key = entries[identifier_idx]
            for i in range(len(headers)):
                header = headers[i]
                data[header][identifier_key] = entries[i]
    return data

# fungsi alternatif untuk csv parser tanpa identifier
def csv_parser_noid(path: str) -> list[dict]:
    data = []
    file = open(path, 'r+')
    headers = split_str(read_header(path))
    for line in file:
        entries = split_str(strip_str(line))
        if len(entries) != len(headers):
            raise ValueError("Ada data yang kosong atau melebihi kolom header!")
        if entries != headers:
            row_dict = {}
            for i in range(len(headers)):
                row_dict[headers[i]] = entries[i]
            data.append(row_dict)
    return data

# user_id;monster_id;level
# 2;1;1
# 3;2;2
# 3;3;1
# 4;4;1
# 5;5;5