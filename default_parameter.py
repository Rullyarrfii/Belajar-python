# Belajar default Argument Value

# def say_hello(name = "eko"):
#     print(f"hello {name}")

# say_hello("eko")
# say_hello() #ini bisa keluar karena ada default nama parameternya
# # say_hello() // ini akan error karena tidak ada default nama parameternya

def say_hello(first_name = "Budi", last_name=""): #menambahkan 2 default value parameter
    print(f"hello {first_name} - {last_name}")

say_hello("eko")
say_hello(last_name="Fibri") #menambahkan vaue lastname
say_hello(last_name="Fibri", first_name="Yanto") #menambahkan value firstname lastname secara acak
say_hello("Fibri","Yanto") #menambahkan value firstname lastname secara acak tanpa menuliskan parameternya / Parm1: FIbri Parm2:Yanto

# digunakan ketika membuat parameter yang ternyata ga wajib, kita bisa menambahkan default value, jadi ketika ada progrm yang mengambilnya, tidak perlu menuliskan valuenya