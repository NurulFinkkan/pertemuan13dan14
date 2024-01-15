# SOAL 3
# • Buat program dengan fungsi untuk menentukan apakah suatu
# bilangan genap atau ganjil
# • function genap(n)
# • return n mod 2 = 0
# •
# • program utama
# • read n
# • if genap(n) 
# • print (‘bil genap’)
# • else
# • print (‘bil ganjil’)

#program bil bulat
bil=0
bil=int(input("masukan bilangan bulat:"))
if bil % 2 ==0:
    print(f"{bil} adalah bilangan genap")
else:
    print(f"{bil} adalah bilangan ganjil")

