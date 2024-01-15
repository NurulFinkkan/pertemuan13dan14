def cari_data(data, target):
    for elemen in data:
        if elemen == target:
            return True  # Data ditemukan
    return False  # Data tidak ditemukan setelah seluruh list diperiksa

# Contoh list dengan 10 elemen
data_list = [3, 7, 2, 8, 1, 6, 4, 9, 5, 10]

# Elemen yang ingin dicari
target_elemen = 11

# Lakukan pencarian
hasil_pencarian = cari_data(data_list, target_elemen)

# Tampilkan hasil
if hasil_pencarian:
    print(f'Data {target_elemen} ditemukan dalam list.')
else:
    print(f'Data {target_elemen} tidak ditemukan dalam list.')