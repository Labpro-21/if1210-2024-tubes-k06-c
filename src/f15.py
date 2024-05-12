"""
F15 - Save
19623116 Nayaka
"""

import os, sys
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)
data_path = os.path.join(os.path.dirname(__file__), 'data')
sys.path.append(data_path)

def save(db: dict, path: str):
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
    csv.write(headers_row + "\n")

    db_length = len(db[headers[0]])
    for i in range(db_length):
        row = ""
        for j in range(db_width):
            if j != db_width - 1:
                row = f"{row}{db[headers[j]][i]};"
            else:
                row = f"{row}{db[headers[j]][i]}"
        csv.write(row)
        if i != db_length - 1:
            csv.write("\n")
    csv.close()


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""