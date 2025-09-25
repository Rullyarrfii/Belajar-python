# belajar break -> menghentikan pengulangan

# for i in range(1,100):
#     if i % 50 == 0: #jika i/50=0 maka pengulangan berakhir
#         break #memberhentikan pengulangan
#     print(i)

# break bisa dipakai untuk while loop juga, tidak hanya for loop

while True:
    data = input("data: ")
    if data == "x":
        break
    print(data)