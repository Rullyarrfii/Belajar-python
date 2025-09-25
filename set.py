# belajar set

# list => []
# tuple => ()
# set => {}

nama = {"eko", "budi", "budi", "eko","budi", "andi"}

nama.add("uwi")
nama.add("uwi")
nama.add("uwi")

# print(nama)

for data in nama:
    print(data)

nama.remove("uwi")

print(nama)

# set, tuple sama list sama hasilnya
# set tidak bisa menambahkan nilai yang sama, nilainya harus unik
# contoh diatas ada 3 nilai, tapi yang ada hanya 2, karna budi nilainya sama
# cocok menyimpan data yang unik tidak duplicate
# tidak bisa mengakses berdasarkan index, hanya menggunakan for loop
# tidak bisa mengubah nilai dengan indeks
# bisa menambah data dengan add
# bisa menghapus data dengan remove