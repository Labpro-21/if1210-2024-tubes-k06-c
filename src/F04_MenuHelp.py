"""
F04 - Menu & Help
16523146 Sacca Kovida Kasmaji
19623116 Nayaka
19623296 Muhammad Ra'if Alkautsar
"""
from global_var import *
from src.x01 import *

def menu(role):
    if role == "admin":
        print_text("data/admin_menu.txt")
    elif role == "agent":
        print_text("data/agent_menu.txt")
    else: # role == "unlogged"
        print_text("data/unlogged_menu.txt")
