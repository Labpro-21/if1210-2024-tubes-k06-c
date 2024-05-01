"""
X01 - Fungsi-fungsi Pembantu
19623116 Nayaka
"""
def is_in(e, arr) -> bool:
    # Type tidak dideklarasikan secara jelas agar dapat digunakan untuk e dengan type int maupun str
    for i in range(len(arr)):
        if e == arr[i]:
            return True
    return False    

def is_space(char: str) -> bool:
    return True if char == " " or char == "\t" or char =="\n" else False

def is_numerical(text: str) -> bool:
    i = 0
    while i < len(text):
        if not is_in(text[i], "0123456789"):
            return False
        i += 1
    return True

def split_str(line: str) -> list:
    row = []
    i = 0
    while (i < len(line)):
        entry = ""
        while (i < len(line)) and (line[i] != ";"):
            entry = f"{entry}{line[i]}"
            i += 1
        
        if is_numerical(entry):
            entry = int(entry)

        row.append(entry)
        i += 1
    return row

def strip_str(line: str) -> str:
    i = 0
    while i < len(line) and is_space(line[i]):
        i += 1
    
    j = len(line) - 1
    while j > i and is_space(line[j]):
        j -= 1
    
    stripped_line = ""
    for i in range(i, j+1):
        stripped_line = f"{stripped_line}{line[i]}"
    
    return stripped_line

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
print(csv_parser("data/user.csv"))
