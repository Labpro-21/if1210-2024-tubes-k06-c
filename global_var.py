import time
start = time.time()

from src.f14 import *

user_db = load('data/user.csv')
monster_db = load('data/monster.csv')
monster_shop_db = load('data/monster_shop.csv')
monster_inv_db = load('data/monster_inventory.csv')
item_shop_db = load('data/item_shop.csv')
item_inv_db = load('data/item_inventory.csv')

logged_in = False