#Belajar Elif

menu_pilihan = input("Masukkan pilihan (1-3): ")

if menu_pilihan == "1":
    print("Anda memilih menu 1")
elif menu_pilihan == "2":
    print("Anda memilih menu 2")
elif menu_pilihan == "3":
    print("Anda memilih menu 3")
else:
    print("Menu tidak tersedia")

    if menu_pilihan == "x":
        print("Program selesai") #Jika buat blok if baru akan tetap dieksekusi