"""
X01 - Fungsi-fungsi Pembantu 2
19623116 Nayaka
"""
from x01 import *
# Jika ingin menjalankan file ini secara independen
# (bukan sebagai module dari main.py) hilangkan "src."

def read_header(path: str) -> str:
    file =  open(path, 'r')
    for line in file:
        return line.strip()

def csv_parser(path: str) -> list[dict]:
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

def get_val(db: list[dict], val, src, tget) -> int:
    for i in range(len(db)):
        if db[i][src] == val:
            return db[i][tget]
    return