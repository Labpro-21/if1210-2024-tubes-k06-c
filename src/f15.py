"""
F15 - Save
19623116 Nayaka
"""

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

    db_length = len(db[headers[0]])
    for i in range(db_length):
        row = ""
        for j in range(db_width):
            if j != db_width - 1:
                row = f"{row}{db[headers[j]][i]};"
            else:
                row = f"{row}{db[headers[j]][i]}"
        csv.write(row)
        csv.write("\n")


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""