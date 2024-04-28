"""
F00 - Random Number Generator
19623116 Nayaka
"""

# FUNGSI lcg(a, c, m, x_0)
def lcg(a: int, c: int, m: int, x_0: int) -> int:
    # Mengembalikan (a * x_0 + c) % m seperti pada rumus LCG
    return (a * x_0 + c) % m

# FUNGSI rng(start, stop, x_0)
def rng(start: int, stop: int, x_0: int = 0) -> int:
    # KAMUS LOKAL
    # a: int            ;multiplier untuk LCG 
    # c: int            ;increment untuk LCG
    # m: int            ;modulus untuk LCG
    # x_n: int          ;bilangan acak ke-n setelah seed
    # rand_num: int     ;bilangan acak yang dikeluarkan

    # ALGORITMA
    # Inisiasi awal variabel lokal fungsi
    a = 69420177013
    c = 1945
    m = 2 ** 21
    x_n = x_0

    # Menciptakan bilangan acak
    while True:
        x_n = lcg(a, c, m, x_n)
        rand_num = x_n % (stop - start) + start # Memastikan bilangan acak ada di selang [start, stop]
        
        if rand_num < stop:
            return rand_num


"""
DESKRIPSI
Penjelasan ini ditaruh sementara dan akan dihapus pada rilis versi final.

Pembangkit bilangan acak semu (pseudo-random number generator) yang kita gunakan di Tubes cool abiez ini adalah linear 
congruential generator (LCG) yang dideskripsikan dengan relasi rekurens berikut [1, 2]:

x_(n+1) = (a * x_n + c) % m

dengan a adalah pengali (multiplier), c adalah penambah (increment), dan m adalah modulus. Suku pertama, x_0, 
disebut sebagai "seed". Diasumsikan m > 0 serta 0 < a, c, x_0 < m.

Akibat penggunaan modulo, LCG sebenarnya menghasilkan barisan bilangan yang berulang (mempunyai periode) sehingga kualitas 
algoritma LCG dilihat dari seberapa besar periode tersebut. Keempat "angka aneh" tadi dipilih berdasarkan teorema berikut [1]:

TEOREMA Hull-Dobell. Untuk c != 0, LCG akan mempunyai periode penuh m jika dan hanya jika
1. c dan m koprima, yang sama saja dengan fpb(c, m) == 1;
2. a % p == 1 jika p adalah faktor prima m;
3. a % 4 == 1 jika 4 adalah faktor m.

Jika kita pilih m sebagai pangkat 2, maka kita cukup pilih c ganjil dan a = 4k + 1 untuk sembarang bilangan asli k.
Pemilihan m ini efisien karena komputer bekerja dengan sistem bilangan biner. Agar periodenya besar, kita pilih 
pangkat 2 yang besar, misalnya 2 ** (11 + 10) karena saya lahir di tanggal 11 Oktober. Selanjutnya, dipilih c = 1945 
agar terdengar nasionalis serta a = 69420177013 yang dipilih secara acak tanpa alasan.

Supaya simpel, kita pilih nilai default seed-nya 0.

DAFTAR PUSTAKA
[1] Hull, T.E. dan Dobell, A.R. (1962). "Random Number Generators." SIAM Review 4(3): 230-254. Diakses 26 April 2024 
    pukul 14:36 WIB.
    https://dspace.library.uvic.ca/server/api/core/bitstreams/b7ffb4ac-e2dd-40fb-bb69-74ae37a79fd8/content 
"""
