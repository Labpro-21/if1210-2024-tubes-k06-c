"""
FB03 - Monster Ball
19623296 / Muhammad Ra'if Alkautsar
"""
# As long as it works. T_T

from src.F00_RandomNumberGenerator import *
from src.F10_ShopCurrency import *
from global_var import *

def monsterball_success(level: int) -> bool:
    result = rng(0, 20, int(time.time()))
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

def check_monsterball(item_inv_db, user_id):
    i = 0
    while i < len(item_inv_db["type"]):
        if item_inv_db["type"][i] == "monsterball" and item_inv_db["user_id"][i] == user_id:
            return(True)
        else:
            i += 1
    return(False)

def use_monsterball(item_inv_db, user_id):
    i = 0
    while i < len(item_inv_db["type"]):
        if item_inv_db["type"][i] == "monsterball" and item_inv_db["user_id"][i] == user_id:
            item_inv_db["quantity"][i] -= 1
            if item_inv_db["quantity"][i] == 0:
                item_inv_db = remove_item(i, item_inv_db)
            break
        else:
            i += 1
    return(item_inv_db)
