# Program Management Kontak
import function

# List of dictionaries to store contacts
daftar_kontak = []
daftar_kontak.append({"nama": "Budi",
                    "email": "Budi@gmail.com","telepon": "08123456789"})       # contoh data awal/Dummy
# Menu Program
while True:
    print("#Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar")

    menu = input("Pilih Menu: ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak_baru = function.new_kontak()
        daftar_kontak.append(kontak_baru)
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia")
print("Program selesai, sampai jumpa!")