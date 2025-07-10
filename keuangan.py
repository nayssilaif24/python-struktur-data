import csv
import os

# Nama file CSV
file_csv = "keuangan.csv"

# Cek dan buat file CSV kalau belum ada atau isinya kosong
if not os.path.exists(file_csv) or os.stat(file_csv).st_size == 0:
    with open(file_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tanggal", "Kategori", "Jenis", "Jumlah", "Deskripsi"])
        
# Fungsi tambah transaksi (Create)
def tambah_transaksi():
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    kategori = input("Kategori (misal: Makan, Transport,belanja,ukt): ")
    jenis = input("Jenis (masuk/keluar): ")
    jumlah = input("Jumlah uang: ")
    deskripsi = input("Deskripsi: ")

    with open(file_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, kategori, jenis, jumlah, deskripsi])

    print("✅ Transaksi berhasil ditambahkan!\n")

# Fungsi lihat semua transaksi (Read)
def lihat_transaksi():
    try:
        with open(file_csv, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)

            if len(data) <= 1:
                print("Belum ada transaksi.\n")
                return

            print("\n=== Daftar Transaksi ===")
            for i, row in enumerate(data):
                if i == 0:
                    print(f"{'No':<5}{' | '.join(row)}")
                else:
                    print(f"{i:<5}{' | '.join(row)}")
            print()

    except FileNotFoundError:
        print("File tidak ditemukan.\n")

# Fungsi update transaksi
def update_transaksi():
    lihat_transaksi()
    no = int(input("Masukkan nomor transaksi yang mau diedit: "))

    with open(file_csv, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    if no < 1 or no >= len(data):
        print("❌ Nomor transaksi tidak valid.\n")
        return

    print("Masukkan data baru:")
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    kategori = input("Kategori: ")
    jenis = input("Jenis (masuk/keluar): ")
    jumlah = input("Jumlah uang: ")
    deskripsi = input("Deskripsi: ")

    data[no] = [tanggal, kategori, jenis, jumlah, deskripsi]

    with open(file_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("✅ Transaksi berhasil diupdate!\n")

# Fungsi hapus transaksi
def hapus_transaksi():
    lihat_transaksi()
    no = int(input("Masukkan nomor transaksi yang mau dihapus: "))

    with open(file_csv, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

    if no < 1 or no >= len(data):
        print("❌ Nomor transaksi tidak valid.\n")
        return

    data.pop(no)

    with open(file_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("✅ Transaksi berhasil dihapus!\n")

# Menu utama
def menu():
    while True:
        print("=== Aplikasi Keuangan Pribadi ===")
        print("1. Tambah Transaksi")
        print("2. Lihat Transaksi")
        print("3. Edit Transaksi")
        print("4. Hapus Transaksi")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_transaksi()
        elif pilihan == "2":
            lihat_transaksi()
        elif pilihan == "3":
            update_transaksi()
        elif pilihan == "4":
            hapus_transaksi()
        elif pilihan == "5":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid!\n")

# Jalankan program
menu()