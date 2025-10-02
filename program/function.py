# Program Management Kontak

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("=====================")
        print(f"Nama: {kontak['nama']}")
        print(f"Email: {kontak['email']}")
        print(f"Telepon: {kontak['telepon']}")
        print("=====================")

def new_kontak():   #tidak menuliskan nama parameter, karena input langsung diambil dari user
    nama = input("Masukkan Nama: ")
    email = input("Masukkan Email: ")
    telepon = input("Masukkan Telepon: ")
    kontak = {
        "nama": nama,
        "email": email,
        "telepon": telepon
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("Masukkan Nomor Telepon yang akan dihapus: ")

    index = -1 # -1 menandakan kontak tidak ditemukan
    
    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index = 1
            break

    if index == -1:
        print("Kontak tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("Kontak berhasil dihapus")

def cari_kontak(daftar_kontak):
    nama_yg_dicari = input("Masukkan Nama yang dicari: ")
    
    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print("=====================")
            print(f"Nama: {kontak['nama']}")
            print(f"Email: {kontak['email']}")
            print(f"Telepon: {kontak['telepon']}")
            print("=====================")
        else:
            print("Kontak tidak ditemukan")

# find = mencari, kalau tidak ditemukan akan mengembalikan nilai -1
# find tidak sensitif terhadap huruf besar/kecil, sehingga perlu diubah ke lower() semua
# find menjadi integer untuk index, kalau tidak ditemukan -1, kalau ditemukan index keberapa
# find hanya untuk string, bukan untuk list atau dictionary
# kalau ingin mencari data yang sama persis, maka bisa menggunakan if nama == nama_yg_dicari
# kalau ingin mencari data yang mengandung kata tertentu, maka bisa menggunakan if nama.find(nama_yg_dicari) != -1
# kalau ingin mencari data yang mengandung kata tertentu tanpa sensitif terhadap huruf besar/kecil, maka bisa menggunakan if nama.lower().find(nama_yg_dicari.lower()) != -1
# find bisa mencari beberapa karakter, tidak harus satu karakter saja