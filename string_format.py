nama_depan = "John"
nama_tengah = "F."
nama_belakang = "Doe"

sapa = "Halo " + nama_depan + " " + nama_tengah + " " + nama_belakang
sapain = "halo{nama_depan} {nama_tengah} {nama_belakang}" #tanpa f-string
sapaan = f"halo{nama_depan} {nama_tengah} {nama_belakang}" # menggunakan f-string

print(sapa)
print(sapain)
print(sapaan)
