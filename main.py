"""
TUGAS BESAR IF1210 DASAR PEMROGRAMAN
K06-C

19623116    Zulfaqqar Nayaka Athadiansyah	
19623296    Muhammad Ra'if Alkautsar
19623076    Daniel A. M. Sipayung
16523106    Naufal Fakhri Fadhlurrahman
16523146    Sacca Kovida Kasmaji

SEKOLAH TEKNIK ELEKTRO DAN INFORMATIKA
INSTITUT TEKNOLOGI BANDUNG
2024
"""

# Mengimpor library yang dibutuhkan
import os, sys, math, time, argparse, datetime

# Mengimpor fungsi-fungsi yang sudah dibuat dengan penuh jerih payah
src_path = os.path.join(os.path.dirname(__file__), 'src')
data_path = os.path.join(os.path.dirname(__file__), 'data')
sys.path.append(src_path)
sys.path.append(data_path)

from x01 import *
from x02 import *

print("Mohon maximize window command prompt Anda untuk pengalaman terbaik.")
time.sleep(3)
for i in range(5):
    remove_nth_line(1)
    print(f"Memulai program dalam {5-i} detik...")
    time.sleep(1)
remove_nth_line(1)
print("Selesai!")
time.sleep(2)
remove_nth_line(1)