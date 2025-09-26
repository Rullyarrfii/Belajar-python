# Belajar Method Return Value

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    # print(f"Total {list_angka} = {total}")
    return total #mengembalikan nilai total

val = jumlahkan(10,10,10,10,10) #menyimpan nilai return total dengan variable val

# mengambil data total?
print(val)

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return (list_angka, total) #mengembalikan nilai list_angka dan total //Tuple

list_angka, total = jumlahkan(10,10,10,10,10) #menyimpan nilai return total dengan variable total //Total => Tuple

# mengambil data total?
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")

# 2 jenis method. Prosedur(mengeksekusi kode program aja yang biasa dibuat) dan Function (method yang mengembalikan nilai)
# return value => bisa mengembalikah hasil/value dari dalam sebuah method