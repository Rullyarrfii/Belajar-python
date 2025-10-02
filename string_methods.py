# Belajar String Methods di Python
# https://docs.python.org/3.7/library/stdtypes.html#string-methods
# method merubah string menjadi uppercase, lowercase, capitalize, title, swapcase, dll
# method memecah string menjadi array of string, dll
# method menggabungkan array of string menjadi string, dll

nama = "ucup surucup"
print(nama)
print(nama.upper())        # mengubah semua karakter menjadi uppercase
# print(nama.lower())        # mengubah semua karakter menjadi lowercase
print(nama.capitalize())   # mengubah karakter pertama menjadi uppercase
print(nama.title())        # mengubah karakter pertama di setiap kata menjadi uppercase
# print(nama.swapcase())     # mengubah karakter uppercase menjadi lowercase dan sebaliknya
print(nama.split(" "))       # memecah string menjadi array/List of string berdasarkan spasi

# penulisan method
# nama.method()