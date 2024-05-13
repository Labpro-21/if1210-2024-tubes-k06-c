"""
FB03 - Monster Ball
19623296 / Muhammad Ra'if Alkautsar
"""
from f00 import *
from global_var import *

def monsterball(level: int) -> bool:
    result = rng(0, 20, time.time())
    if level == 1:
        if 0 < result < 15:
            return(True)
        else: 
            return(False)
    elif level == 2:
        if 0 < result < 10:
            return(True)
        else:
            return(False)
    elif level == 3:
        if 0 < result < 5:
            return(True)
        else:
            return(False)
    elif level == 4:
        if 0 < result < 2:
            return(True)
        else:
            return(False)
    else:
        if 0 < result < 1:
            return(True)
        else:
            return(False)

""" def monster_caught(): # KODE RUSAK
    i = 0
    temp_db = {"user_id":[], "monster_id":[], "level":[]}
    while temp_db["user_id"][i] <= user:
        temp_db["user_id"].append(monster_inv_db["user_id"][i])
        temp_db["monster_id"].append(monster_inv_db["monster_id"][i])
        temp_db["level"].append(monster_inv_db["level"][i])
        i += 1
    temp_db["user_id"].append(monster_inv_db["user_id"][i])
    temp_db["monster_id"].append(monster_inv_db["monster_id"][i])
    temp_db["level"].append(monster_inv_db["level"][i])
    i += 1 
    while i <= (len(monster_inv_db["user_id"]) + 1):
        temp_db["user_id"].append(user)
        temp_db["monster_id"].append(random_index + 1)
        temp_db["level"].append(enemy_level)
        i += 1
    monster_inv_db = temp_db """

"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.


"""