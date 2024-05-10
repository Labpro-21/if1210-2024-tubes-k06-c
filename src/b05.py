"""
FB05 - Peta Kota Danville
19623296 / Muhammad Ra'if Alkautsar
"""

def read_map(N : int, M : int, fn : str):
    arr = [["" for j in range(M)] for i in range(N)]
    with open(fn, 'r') as map:
        i = int(0)
        for line in map:
            j = int(0)
            for symbol in line.strip(): 
                arr[i][j] = symbol
                j += 1
            i += 1
    return(arr)

def print_map(map):
    for i in range(M):
        for j in range(N):
            print(f"{map[i][j]}", end="")
        print()

N = 10
M = 10
posx = 0
posy = 0
map = read_map(N, M, "data/map.txt")

def moveUp():
    global posy
    if posy == 0:
        print("Ada penghalang!")
        move()
    elif (map[posy-1][posx]) != '#':
        print("Ada penghalang!")
        move()
    else:
        map[posy][posx] = "#" 
        posy -= 1
        map[posy][posx] = "P"

def moveDown():
    global posy
    if posy == (N-1):
        print("Ada penghalang!")
        move()
    elif (map[posy+1][posx]) != '#':
        print("Ada penghalang!")
        move()
    else:
        map[posy][posx] = "#"  
        posy += 1
        map[posy][posx] = "P"
    
def moveLeft():
    global posx
    if posx == 0:
        print("Ada penghalang!")
        move()
    elif (map[posy][posx-1]) != '#':
        print("Ada penghalang!")
        move()
    else:
        map[posy][posx] = "#"   
        posx -= 1
        map[posy][posx] = "P"

def moveRight():
    global posx
    if posx == (M-1):
        print("Ada penghalang!")
        move()
    elif (map[posy][posx+1]) != '#':
        print("Ada penghalang!")
        move()
    else:
        map[posy][posx] = "#"  
        posx += 1
        map[posy][posx] = "P"

def move():
    gerak = input("Ke arah mana Anda ingin berpindah?")
    if gerak == "up":
        moveUp()
    elif gerak == "right":
        moveRight()
    elif gerak == "left":
        moveLeft()
    elif gerak == "down":
        moveDown()
    else: 
        print("Pergerakan tidak valid!")
        move()

while True:
    move()
    print_map(map)

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
"""