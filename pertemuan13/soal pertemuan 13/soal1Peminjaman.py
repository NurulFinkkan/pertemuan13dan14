# SOAL 1
# • Buat program untuk menentukan durasi lamanya waktu peminjaman. 
# • Jika lama > 7, maka terlambatj ika parameternya tgl pinjam dan tgl kembali
# • Hitung keterlambatan per hari * 2000.
# • Contoh tampilan hasil :

# notif
print("\n")
print ("tarif perhari 5000'-")
print("\n")

# input nilai tangal pinjam
TP=int(input("tanggal pinjam = ")) 
TK=int(input("tanggal kembali = "))
BP=str(input("bulan = "))
if TP > 31:
    print('silahkan chek kembali di bagian ' '\033[1m' + 'tanggal pinjam')
if TK > 31 :
    print('Silahkan chek kembali ' '\033[1m' + ' tangal kembali')

hasil = TK - TP
print(f"tanggal pinjam {TP} {BP} " f"Tanggal Kembali {TK} {BP} Total bayar = {hasil * 5000},- ")

print("\n")
print ("jika terlambat dikenakan denda perhari 2000,-")
print("\n")

TP2=int(input("tanggal pinjam = ")) 
TK2=int(input("tanggal kembali = "))
BP=str(input("bulan = "))
if TK != TK2 :
    Hukum= TK2 - TK
    print(f"Terlambat {Hukum}" f" kena denda{Hukum*2000},-")
else:
    print("terima kasih")

