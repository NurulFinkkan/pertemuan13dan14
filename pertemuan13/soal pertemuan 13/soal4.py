from datetime import datetime

def hitung_keterlambatan(tgl_pinjam, tgl_kembali):
    # Mengubah string tanggal menjadi objek datetime
    tgl_pinjam = datetime.strptime(tgl_pinjam, '%Y-%m-%d')
    tgl_kembali = datetime.strptime(tgl_kembali, '%Y-%m-%d')

    # Menghitung durasi peminjaman dalam hari
    durasi_peminjaman = (tgl_kembali - tgl_pinjam).days

    if durasi_peminjaman > 7:
        keterlambatan = (durasi_peminjaman - 7) * 2000
        print(f'Anda terlambat {durasi_peminjaman - 7} hari. Biaya keterlambatan: Rp {keterlambatan}.')
    else:
        print('Anda mengembalikan tepat waktu.')

# Contoh penggunaan
tgl_pinjam = input('Masukkan tanggal pinjam (format: YYYY-MM-DD): ')
tgl_kembali = input('Masukkan tanggal kembali (format: YYYY-MM-DD): ')

hitung_keterlambatan(tgl_pinjam, tgl_kembali)