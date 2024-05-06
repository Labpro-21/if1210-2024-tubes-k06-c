"""
X01 - Fungsi-fungsi Pembantu 1
19623116 Nayaka
19623296 Ra'if
"""
import sys
def maxi(a: int, b: int) -> int:
    if a >= b:
        return a
    return b

def mini(a: int, b: int) -> int:
    if a >= b:
        return b
    return a

def is_in(e, arr) -> bool:
    # Type tidak dideklarasikan secara jelas agar dapat digunakan untuk e dengan type int maupun str, 
    # serta arr untuk array of integer, string, ataupun sebuah dictionary
    if (type(arr) == list) or (type(arr) == str):
        for i in range(len(arr)):
            if e == arr[i]:
                return True
    elif (type(arr) == dict):
        for key in arr.keys():
            if e == key:
                return True
    return False    

def subset(arr1, arr2) -> bool:
    # Type tidak dideklarasikan secara jelas agar dapat digunakan untuk e dengan type int maupun str
    if len(arr1) > len(arr2):
        return False
    for i in range(len(arr1)):
        if not is_in(arr1[i], arr2):
            return False
    return True

def remove_nth_line(n: int):
    # Bergerak ke baris di atasnya
    for i in range(n):
        sys.stdout.write('\x1b[1A')
    # Menghapus baris (clear)
    sys.stdout.write('\x1b[2K')

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

def remove_ele(index: int, arr: list) -> list:
    newArr = []
    for i in range(len(arr)):
        if i != index:
            newArr.append(arr[i])
    return newArr

def printText(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            print(line, end='')