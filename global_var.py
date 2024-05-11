import time,os
start = time.time()

from src.f14 import *
path=str(os.path.dirname(__file__))
user_db = load(rf'{path}\data\user.csv')
monster_db = load(rf'{path}\data\monster.csv')
monster_shop_db = load(rf'{path}\data\monster_shop.csv')
monster_inv_db = load(rf'{path}\data\monster_inventory.csv')
item_shop_db = load(rf'{path}\data\item_shop.csv')
item_inv_db = load(rf'{path}\data\item_inventory.csv')

logged_in = False