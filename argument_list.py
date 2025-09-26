# Belajar Argument List

# Contoh 1
def jumlahkan(satu, dua, tiga, empat=5): #method jumlahkan, param satu dan dua, param 4 nilai int 0
    total = satu + dua + tiga +empat
    print(f"Total {[satu,dua,tiga]} = {total}")

jumlahkan(10, 10, 10) #execute method jumlahkan, isikan param satu dan dua // walaupun ga ditulis param 4, tapi hasilnya 35. karna param 4 nilainya udah ditulis

# Contoh 2 // Argument List
# def jumlahkan(*list_angka):
def jumlahkan(x, *list_angka): #menambahkan bintang di depan param akan menjadi argumen list, yang dapat memasukkan banyak data
    # argumen list tidak bisa diisi 2x
    # argumen list wajib dibelakang param yang lain (x,*list_angka)
    total = 0
    for angka in list_angka :
        total = total + angka
    print(f"Total {list_angka} = {total}")

jumlahkan(10, 10, 10) #jika ditambah param 1 x, dan param 2 argumen list. jika 3 nilai. maka 1 nilai untuk param 1, 2 nilai belakangnya param 2