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

# Mengimpor fungsi-fungsi yang sudah dibuat
for namafile in os.listdir(os.path.abspath("src")):
    if namafile[-3:] == ".py":
        namamodule = "src." + namafile[:-3]
        __import__(namamodule)
