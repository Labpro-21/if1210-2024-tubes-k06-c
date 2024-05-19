import time
start = time.time()

from src.F14_Load import *

user_db = load_csv('data/user.csv')
monster_db = load_csv('data/monster.csv')
monster_shop_db = load_csv('data/monster_shop.csv')
monster_inv_db = load_csv('data/monster_inventory.csv')
item_shop_db = load_csv('data/item_shop.csv')
item_inv_db = load_csv('data/item_inventory.csv')