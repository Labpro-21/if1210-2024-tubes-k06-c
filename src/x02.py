"""
X02 - Fungsi-fungsi Pembantu 2
19623116 Nayaka
"""
import os, sys
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)
data_path = os.path.join(os.path.dirname(__file__), 'data')
sys.path.append(data_path)

from x01 import *
# Jika ingin menjalankan file ini secara independen
# (bukan sebagai module dari main.py) hilangkan "src."

def read_header(path: str) -> str:
    file = open(path, 'r')
    for line in file:
        return line.strip()

def csv_parser(path: str) -> dict:
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

def database_to_csv(db: dict, path: str):
    csv = open(path, "w")
    db_width = len(db)
    headers = []
    headers_row = ""

    i = 0
    for header in db.keys():
        headers.append(header)

        if i != db_width - 1:
            headers_row = f"{headers_row}{header};"
        else:
            headers_row = f"{headers_row}{header}"

        i += 1

    print(headers_row)

    db_length = len(db[headers[0]])
    for i in range(db_length):
        row = ""
        for j in range(db_width):
            if j != db_width - 1:
                row = f"{row}{db[headers[j]][i]};"
            else:
                row = f"{row}{db[headers[j]][i]}"
        print(row)
        csv.write(row)
        csv.write("\n")
