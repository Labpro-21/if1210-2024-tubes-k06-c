"""
X01 - Fungsi-fungsi Pembantu 2
19623116 Nayaka
"""
import os, sys
# Mengimpor fungsi-fungsi yang sudah dibuat dengan penuh jerih payah
src_path = os.path.join(os.path.dirname(__file__), 'src')
data_path = os.path.join(os.path.dirname(__file__), 'data')
sys.path.append(src_path)
sys.path.append(data_path)

from x01 import *
# Jika ingin menjalankan file ini secara independen
# (bukan sebagai module dari main.py) hilangkan "src."

def read_header(path: str) -> str:
    file = open(path, 'r')
    for line in file:
        return line.strip()

def csv_parser(path: str, identifier: str) -> list[dict]:
    file = open(path, 'r+')
    headers = split_str(read_header(path))
    data = {header : {} for header in headers}
    
    identifier_idx = -1
    for i in range(len(headers)):
        if headers[i] == identifier:
            identifier_idx = i
    if identifier_idx == -1:
        raise ValueError("Identifier tidak ditemukan!")

    # Menambahkan data pada tiap kolom satu per satu
    for line in file:
        entries = split_str(strip_str(line))
        if len(entries) != len(headers):
            raise ValueError("Ada data yang kosong atau melebihi kolom header!")
        if entries != headers:
            identifier_key = entries[identifier_idx]
            for i in range(len(headers)):
                header = headers[i]
                data[header][identifier_key] = entries[i]
    return data

def get_val(db: list[dict], val, src, tget) -> int:
    for i in range(len(db)):
        if db[i][src] == val:
            return db[i][tget]
    return
