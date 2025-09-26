# Belajar tipe data dictionary
# List, Set, Tuple, Dictionary => bisa menyimpan lebih banyak data
# list ataupun tuple, akses dengan indeks, jika indeksnya salah, maka datanya salah
# tipe data dictionary bisa mengganti indeksnya menjadi string, nilainya bebas
# {"key":"value",} membuat dictionary
# kemungkinan salah untuk memasukkan indeksnya sangat kecil
# dictionary bisa untuk for loop

customer = {"Name":"Eko","Age":30,"Address":"SUbang"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["company"] = "X" #menambahkan data
customer["Name"] = "Eko Kurniawan" #mengubah data nama

del customer["Address"] #menghapus data di dictionary

# for key in customer:
#     value = customer[key]
#     print(f"{key} : {value}")

# menggunakan hasil dari method items
for key in customer.items():
    print(f"{key[0]} : {key[1]}")

# mengubah indeks menjadi key dan value
for key, value in customer.items():
    print(f"{key} : {value}")

# di dictionary ada method namanya items
# print(customer.items())

# dictionary digunakan menambahkan,mengubah, menghapus data seperti list
# jika membuat data customer, dibuat dalam bentuk dictionary jangan dalam bentuk list, tuple, set. agar mudah mengakses dengan cara mention data keynya