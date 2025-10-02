# Belajar Module
# module adalah sebuah file yang berisi kode Python yang dapat digunakan kembali di program lain.
# Module memungkinkan kita untuk mengorganisir kode kita ke dalam file-file terpisah, sehingga lebih mudah untuk dikelola dan dipelihara.
# file untuk database, proses webnya, fitur yang lain. file itu disebut module.

# Contoh 1
# import function # mengimport module function.py

# hello = function.say_hello("Andi") # memanggil function say_hello dari module function
# print(hello)

# hasil = function.total(1,2,3,4,5) # memanggil function total dari module function
# print(hasil)

# contoh 2
from function import say_hello # mengimport function tertentu dari module function.py
from function import total # mengimport function tertentu dari module function.py

hello = say_hello("Budi") # memanggil function say_hello dari module function, tidak perlu menuliskan nama module
print(hello)