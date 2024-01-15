print("\n")
#input nlai
x=int(input("masukan nilai x ="))
y=int(input("Masukan nilai y ="))
#fungsi penjumlahan
def jumlah(x, y) :
    return x + y
#fungsi pengurangan
def kurang(x,y) :
    return x - y
#fungsi perkalian
def kali(x,y) :
    return x * y
#fungsi pembagian
def bagi(x, y) :
    return x / y
#membuat main loop progamya
def show_menu():
    print ("--------- MENU--------")
    print ("[1]  penjumlahan")
    print ("[2]  Pengurangan")
    print ("[3]  Perkalian")
    print ("[4]  Pembagian")
if __name__ == "__main__":
    while(True): 
        show_menu()
        break
menu = input("PILIH MENU> ")
if menu == '1':
    print('hasil jumlah : ', jumlah(x,y)) 
elif menu == '2':
    print('hasil kurang : ', kurang(x,y))
elif menu == '3':
    print('hasil kali : ', kali(x,y))
elif menu == '4':
    print('hasil bagi : ', bagi(x,y))
else :
    print('tidak ada menu !')




