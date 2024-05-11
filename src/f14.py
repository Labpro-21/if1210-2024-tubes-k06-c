"""
F14 - Load
19623116 Nayaka
"""
import os, sys
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)
data_path = os.path.join(os.path.dirname(__file__), 'data')
sys.path.append(data_path)

from x01 import *

def read_header(path: str) -> str:
    file = open(path, 'r')
    for line in file:
        return strip_str(line)
    return ""

def load(path: str) -> dict:
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
    return data

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""