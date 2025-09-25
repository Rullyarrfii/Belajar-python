#Belajar For loop

pelanggan = ["eko", "budi", "joko", "andi"]

pelanggan.append("Hengky")
pelanggan.append("Asih")

#mengakses semua nama pelanggan tanpa for

print(pelanggan[0])
print(pelanggan[1])
print(pelanggan[2])
print(pelanggan[3])

print()
#mengakses semua nama pelanggan dengan for

for nama in pelanggan:
    # print(nama)
    print(f"Nama Pelanggan: {nama}")
#Data yang ada di for akan terulang ulang lagi