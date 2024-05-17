"""
FB05 - Peta Kota Danville
19623296 / Muhammad Ra'if Alkautsar
"""

def read_map(N : int, M : int, fn : str):
    arr = [["" for j in range(M+2)] for i in range(N+2)] # Array diinisialisasi 
                                                         # dengan ruang 
                                                         # tambahan untuk garis pembatas tepian map.
    with open(fn, 'r') as map:
        for p in range(M+2):
            arr[0][p] = "*"
        i = int(1)
        for line in map:
            arr[i][0] = "*"
            j = int(1)
            for symbol in line.strip(): 
                arr[i][j] = symbol
                j += 1
            arr[i][M+1] = "*"
            i += 1
        for p in range(M+2):
            arr[N+1][p] = "*"
    return(arr)


# DATA SAMPEL UNTUK KEBUTUHAN TESTING !!! TIDAK TERMASUK PROSEDUR/FUNGSI
N = 10
M = 10
posx = 1
posy = 1
map = read_map(N, M, "data/map.txt")

def print_map(map):
    for i in range(M+2):
        for j in range(N+2):
            obj = map[i][j]
            if obj == "#":
                print("  ", end="")
            else:
                print(f"{map[i][j]} ", end="")
        print()

def moveUp():
    global posy
    if (map[posy-1][posx]) != '#':
        print("Ada penghalang!")
        move()
    else:
        map[posy][posx] = "#" 
        posy -= 1
        map[posy][posx] = "P"

def moveDown():
    global posy
    if (map[posy+1][posx]) != '#':
        print("Ada penghalang!")
        move()
    else:
        map[posy][posx] = "#"  
        posy += 1
        map[posy][posx] = "P"
    
def moveLeft():
    global posx
    if (map[posy][posx-1]) != '#':
        print("Ada penghalang!")
        move()
    else:
        map[posy][posx] = "#"   
        posx -= 1
        map[posy][posx] = "P"

def moveRight():
    global posx
    if (map[posy][posx+1]) != '#':
        print("Ada penghalang!")
        move()
    else:
        map[posy][posx] = "#"  
        posx += 1
        map[posy][posx] = "P"

def checkProximity(action):
    # Memeriksa apakah aksi adalah sesuatu yang bisa dilakukan terlepas dari posisi terlebih dahulu.
    if action == "logout" or action == "laboratory" or action == "help": 
        return(True)
    else: # Jika tidak, lantas memeriksa apakah objek aksi tersedia di sekitar posisi pemain
        symbol = chr(action.title()[0])
        # Aksi dan objek dicocokkan dengan mengambil huruf pertama di aksi, karena pada data map, objek disimpan sebagai huruf awal
        for i in range(-1, 2):
            if map[posy-1][posx+i] == symbol:
                return(True)
        if map[posy][posx-1] == symbol:
            return(True)
        if map[posy][posx+1] == symbol:
            return(True)
        for i in range(-1, 2):
            if map[posy+1][posx+i] == symbol:
                return(True)

actionList = ["logout", "inventory", "shop", "battle", "arena", "laboratory", "help"]

def move():
    print_map(map)
    gerak = input("Ke arah mana Anda ingin berpindah?").lower()
    if gerak == "up" or gerak == "u":
        moveUp()
    elif gerak == "right" or gerak == "r":
        moveRight()
    elif gerak == "left" or gerak == "l":
        moveLeft()
    elif gerak == "down" or gerak == "d":
        moveDown()
    elif gerak in actionList:
        if checkProximity():
            gerak() # Jika di sekitar pemain ditemukan objek untuk aksi, maka fungsi/prosedur untuk aksi akan dijalankan.
        else: 
            print("Pergerakan tidak valid!")
    else: 
        print("Pergerakan tidak valid!")

"""
DESKRIPSI

Fitur map dilakukan dengan terlebih dahulu dengan membaca map menggunakan fungsi read_map().
Setelah itu posisi pemain diinisialisasi supaya kita tidak terus-menerus memeriksa di mana pemain berada di peta.
Setelah itu, barulah kita melakukan looping prosedur move().

"""
