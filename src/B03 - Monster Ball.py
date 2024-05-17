"""
FB03 - Monster Ball
19623296 / Muhammad Ra'if Alkautsar
"""
# As long as it works. T_T

from src.f00 import *
from src.f10 import *
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


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.
"""
