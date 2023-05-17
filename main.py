import random

# acak angka dari komputer
angka_min = 1
angka_max = 10
angka_rahasia = random.randint(angka_min, angka_max)

# inputan pengguna
tebakan = int(input("Tebak angka antara 1 dan 10: "))

# ulangi proses jika pengguna salah
while tebakan != angka_rahasia:
    if tebakan < angka_rahasia:
        print("Tebakanmu terlalu rendah.")
    else:
        print("Tebakanmu terlalu tinggi.")
    tebakan = int(input("Coba lagi: "))

print("Selamat! Tebakanmu benar.")