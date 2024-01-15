def cari_data(data, target):
    indeks_pertama = None
    jumlah_pengulangan = 0

    for i, elemen in enumerate(data):
        jumlah_pengulangan += 1
        if elemen == target:
            indeks_pertama = i
            break  # Keluar dari loop setelah menemukan pertama kali

    return indeks_pertama, jumlah_pengulangan

# Contoh list dengan 10 elemen
data_list = [3, 7, 2, 8, 1, 6, 4, 9, 5, 10]

# Elemen yang ingin dicari
target_elemen = 8

# Lakukan pencarian
indeks, jumlah_pengulangan = cari_data(data_list, target_elemen)

# Tampilkan hasil
if indeks is not None:
    print(f'Data {target_elemen} ditemukan pada indeks {indeks}.')
else:
    print(f'Data {target_elemen} tidak ditemukan dalam list.')

print(f'Jumlah pengulangan: {jumlah_pengulangan}')
