#belajar input number

print("Masukkan angka pertama: ")
a = input()

print("Masukkan angka kedua: ")
b = input()

jumlah = a + b
print(f"{a} + {b} = {jumlah}") #2025, karna setiap input jika tidak di validasi type data, maka defaulnya string

print("Masukkan angka pertama: ")
a = int(input())

print("Masukkan angka kedua: ")
b = int(input())

jumlah = a + b
print(f"{a} + {b} = {jumlah}") #30, karna sudah di validasi type data menjadi integer