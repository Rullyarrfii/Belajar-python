# Belajar Module
# membuat file function.py

def say_hello(nama): #definisikan function dengan method say_hello
    return f"Hello {nama}"

def total(*list_angka):
    hasil = 0
    for data in list_angka:
        hasil += data
    return hasil