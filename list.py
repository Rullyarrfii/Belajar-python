#Belajar List

#Panggil nama dengan list
nama = []
nama.append("Andi")
nama.append("Owi")
nama.append("Panji")
print(nama)

#cara kedua
nama = ["Andi", "Owi", "Panji"]
nama.append("Budi")
print(nama)
print(nama[0]) #panggil nama pertama
print(nama[1]) #panggil nama kedua
print(nama[2]) #panggil nama ketiga
print(nama[3]) #panggil nama keempat
print(len(nama)) #menghitung jumlah list
nama.remove("Budi") #menghapus list, urutan data akan berubah
nama.remove("Owi")
print(nama)
print(nama[0]) #panggil nama pertama
print(nama[1]) #panggil nama kedua //berubah urutan data setelah menghapus list

#pangil nama dengan menuliskan nama1, nama2, nama3
nama1 = "Andi"
nama2 = "Owi"
nama3 = "Panji"
print(nama1, nama2, nama3)