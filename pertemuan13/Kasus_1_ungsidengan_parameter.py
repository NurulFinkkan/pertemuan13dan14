def kondisi(nilai_ujian_satu, Nilai_ujian_dua):
    hasil = (nilai_ujian_satu + Nilai_ujian_dua)/2

    if hasil >= 70:
        print("nilai",hasil,"anda lulus")
    elif hasil >=56:
        print("nilai anda",hasil,"anda bisa di remedial")
    else:   
        print("nilai anda",hasil,"anda tidak lulsus")

def main():
    print("jalankan fungsi pada main")
    nilai1=int(input('nilai ke-1: '))
    nilai2=int(input('nilai ke-2: '))
    print(f'nilai ujian 1 : {nilai1} dan nilai ujian 2 : {nilai2}')
    34
    kondisi(nilai1,nilai2)
if __name__=="__main__":
    main()
