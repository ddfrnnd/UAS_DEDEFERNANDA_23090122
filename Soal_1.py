mahasiswa = []

while True:
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    mahasiswa.append({"NIM": nim, "Nama": nama})

    lagi = input("Ingin tambah lagi? (ya/tidak): ")
    if lagi.lower() == "ya":
        continue
    else:
        break

print("Data Mahasiswa:")
for i, data in enumerate(mahasiswa, start=1):
    print(f"{i}. NIM: {data['NIM']}, Nama: {data['Nama']}")

print("Program selesai.")