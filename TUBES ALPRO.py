"""TUGAS BESAR ALPRO MEMBUAT STRUK PEMBAYARAN LISTRIK MENGGUNAKAN INPUTAN DAN MEMASUKKAN OUTPUTAN KEDALAM SEBUAH FILE"""

print("===== SELAMAT DATANG DI LOKET PEMBAYARAN KELOMPOK 8 =====")

# Menampilkan kategori-kategori daya
def tampilkan_daftar_harga():
    print("\n===== DAFTAR HARGA PER KATEGORI =====")
    print("1. Kategori 1 (900 VA) - Rp1.352 per kWh")
    print("2. Kategori 2 (1.300 VA) - Rp1.444 per kWh")
    print("3. Kategori 3 (2.200 VA) - Rp1.444 per kWh")
    print("4. Kategori 4 (3.500-5.500 VA) - Rp1.699 per kWh")
    print("5. Kategori 5 (6.600 VA) - Rp1.699 per kWh")
    print("6. Kategori 6 (6.600 VA - 200 kVa) - Rp1.444 per kWh")
    print("7. Kategori 7 (Daya di atas 200 kVa) - Rp1.114 per kWh")
    print("8. Kategori 8 (Daya di atas 30.000 kVa) - Rp996 per kWh")
    print("=====================================")
tampilkan_daftar_harga()    

def hitung_pembayaran(daya, pemakaian_kWh):
    # Menentukan tarif berdasarkan kategori daya
    if daya == 1:
        tarif = 1352
    elif daya == 2 or daya == 3:
        tarif = 1444
    elif daya == 4 or daya == 5 or daya == 6:
        tarif = 1699
    elif daya == 7:
        tarif = 1114
    elif daya == 8:
        tarif = 996
    else:
        return "Kategori daya tidak valid.", 0  # Mengembalikan tuple yang menyatakan kesalahan

    # Menghitung total pembayaran
    total_pembayaran = tarif * pemakaian_kWh
    return total_pembayaran, tarif

# Definisi fungsi untuk menghitung kembalian
def hitung_kembalian(total_pembayaran, jumlah_pembayaran):
    # Memeriksa apakah jumlah pembayaran cukup
    if jumlah_pembayaran < total_pembayaran:
        return "Jumlah pembayaran kurang. Mohon masukkan jumlah pembayaran yang cukup."
    else:
        kembalian = jumlah_pembayaran - total_pembayaran
        return kembalian

# Definisi fungsi untuk mencetak struk pembayaran dan menyimpannya ke dalam file
def cetak_struk(daya, pemakaian_kWh, total_pembayaran, jumlah_pembayaran, kembalian, tarif):
    # Membuat string struk dengan informasi transaksi
    struk = f"\n===== STRUK PEMBAYARAN LISTRIK =====\n"
    struk += f"Kategori Daya: {daya}\n"
    struk += f"Jumlah Pemakaian kWh: {pemakaian_kWh} kWh\n"
    struk += f"Tarif per kWh: Rp{tarif:.2f}\n"
    struk += f"Total Pembayaran: Rp{total_pembayaran:.2f}\n"
    struk += f"Jumlah Pembayaran: Rp{jumlah_pembayaran:.2f}\n"
    struk += f"Kembalian: Rp{kembalian:.2f}\n"
    struk += "Terima kasih atas pembayaran Anda!"

    # Menampilkan struk di konsol
    print(struk)

    # Menyimpan struk ke dalam file "struk_pembayaran.txt"
    with open("struk_pembayaran.txt", "w") as file:
        file.write(struk)

# Fungsi utama program
def main():
    # Input kategori daya dan jumlah pemakaian kWh
    daya = int(input("Masukkan kategori daya (1-8): "))
    pemakaian_kWh = float(input("Masukkan jumlah pemakaian kWh: "))

    # Hitung total pembayaran berdasarkan input
    hasil_hitung, tarif = hitung_pembayaran(daya, pemakaian_kWh)

    # Cek jika kategori daya tidak valid
    if type(hasil_hitung) == str:
        print(hasil_hitung)
        return

    # Unpack hasil_hitung menjadi total_pembayaran
    total_pembayaran = hasil_hitung

    # Tampilkan total pembayaran dan tarif per kWh
    print(f"Tarif per kWh: Rp{tarif:.2f}")
    print(f"Total pembayaran: Rp{total_pembayaran:.2f}")

    # Input jumlah pembayaran
    jumlah_pembayaran = float(input("Masukkan jumlah pembayaran: "))

    # Hitung kembalian
    kembalian = hitung_kembalian(total_pembayaran, jumlah_pembayaran)

    # Cetak struk dan simpan ke dalam file jika tidak ada masalah dengan pembayaran
    if type(kembalian) == str:
        print(kembalian)
    else:
        cetak_struk(daya, pemakaian_kWh, total_pembayaran, jumlah_pembayaran, kembalian, tarif)

# Menjalankan fungsi utama jika program dijalankan
if __name__ == "__main__":
    main()
