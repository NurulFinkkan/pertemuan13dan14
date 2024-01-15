def data() :
    listku = []
    n=int(input('banyak data : '))
    i=1
    while i<=n :
        angka =int(input("tambah data list : "))
        listku.append(angka)
        i=i+1
    return listku

x=data()
def hitung_rata(x):
    jumlah=0
    for item in x :
        jumlah+=item
    rata=jumlah/len(x)
    return rata

#hitung rata-rata
print('rangkaian data :', x)
print('rata-rata data :', hitung_rata(x))
