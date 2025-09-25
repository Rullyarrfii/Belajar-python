# Membuat Program Menggunakan For-Loop, List dan Range

banyak = int(input("berapa banyak data? ")) #merubah data string ke int saat input

nama = []
umur = []

for i in range(0, banyak):
    print(f"Data ke {i}")
    input_nama = input("Nama: ")
    input_umur = int(input("Umur: "))

    nama.append(input_nama)
    umur.append(input_umur)

print(nama)
print(umur)

# print(len(nama))

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur [i]
    print(f"{data_nama} berumur {data_umur} tahun")