import Soal_3

def main():
    antrian = Soal_4.AntrianRestoran()

    while True:
        print("\n1. Tambah pesanan")
        print("2. Hidangkan pesanan")
        print("3. Tampilkan antrian")
        print("4. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            pesanan = input("Masukkan pesanan: ")
            antrian.tambah_pesanan(pesanan)
        elif pilihan == "2":
            antrian.hapus_pesanan()
        elif pilihan == "3":
            antrian.tampilkan_antrian()
        elif pilihan == "4":
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()