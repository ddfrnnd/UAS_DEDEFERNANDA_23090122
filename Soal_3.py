class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def tambah_pesanan(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' ditambahkan ke antrian.")

    def hapus_pesanan(self):
        if not self.antrian:
            print("Tidak ada pesanan di antrian.")
            return None
        pesanan = self.antrian.pop(0)
        print(f"Pesanan '{pesanan}' dihidangkan.")
        return pesanan

    def tampilkan_antrian(self):
        print("Pesanan saat ini di antrian:")
        for i, pesanan in enumerate(self.antrian, start=1):
            print(f"{i}. {pesanan}")
