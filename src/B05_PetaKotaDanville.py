"""
FB05 - Peta Kota Danville
19623296 Muhammad Ra'if Alkautsar
"""

def read_map(N : int, M : int, fn : str, posx : int, posy : int):
    arr = [["" for j in range(M+2)] for i in range(N+2)] # Array diinisialisasi dengan ruang tambahan untuk garis pembatas tepian map.
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
    arr[posx][posy] = "P" # Posisi pemain diinisialisasi
    return(arr)

def print_map(arr, M, N): 
    for i in range(M+2):
        for j in range(N+2):
            obj = arr[i][j]
            if obj == "#":
                print("  ", end="")
            else:
                print(f"{arr[i][j]} ", end="")
        print()

def moveUp(worldmap, posx, posy):
    if (worldmap[posy-1][posx]) != '#':
        print("Ada penghalang!")
    else:
        worldmap[posy][posx] = "#" 
        posy -= 1
        worldmap[posy][posx] = "P"
    return(worldmap, posx, posy)

def moveDown(worldmap, posx, posy):
    if (worldmap[posy+1][posx]) != '#':
        print("Ada penghalang!")
    else:
        worldmap[posy][posx] = "#"  
        posy += 1
        worldmap[posy][posx] = "P"
    return(worldmap, posx, posy)
    
def moveLeft(worldmap, posx, posy):
    if (worldmap[posy][posx-1]) != '#':
        print("Ada penghalang!")
    else:
        worldmap[posy][posx] = "#"   
        posx -= 1
        worldmap[posy][posx] = "P"
    return(worldmap, posx, posy)

def moveRight(worldmap, posx, posy):
    if (worldmap[posy][posx+1]) != '#':
        print("Ada penghalang!")
    else:
        worldmap[posy][posx] = "#"  
        posx += 1
        worldmap[posy][posx] = "P"
    return(worldmap, posx, posy)


def checkProximity(action, posx, posy, worldmap):
    symbol = action.title()[0]
    # Aksi dan objek dicocokkan dengan mengambil huruf pertama di aksi, karena pada data map, objek disimpan sebagai huruf awal
    for i in range(-1, 2):
        if worldmap[posy-1][posx+i] == symbol:
            return(True)
    if worldmap[posy][posx-1] == symbol:
        return(True)
    if worldmap[posy][posx+1] == symbol:
        return(True)
    for i in range(-1, 2):
        if worldmap[posy+1][posx+i] == symbol:
            return(True)
    return(False)

"""
DESKRIPSI

Fitur map dilakukan dengan terlebih dahulu dengan membaca map menggunakan fungsi read_map().
Setelah itu posisi pemain diinisialisasi supaya kita tidak terus-menerus memeriksa di mana pemain berada di peta.
Setelah itu, barulah kita melakukan looping prosedur move().

"""
