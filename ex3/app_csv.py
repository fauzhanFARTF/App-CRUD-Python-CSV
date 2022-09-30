import csv
import os

csv_filename = '/Users/fauzan_nurrachman/Sites/course/git/Python/App-CRUD-Python-CSV/ex4/mahasiswa.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI DATA MAHASISWA ===")
    print("[1] Lihat Daftar Mahasiswa")
    print("[2] Buat Kontak Mahasiswa")
    print("[3] Edit Mahasiswa")
    print("[4] Hapus Mahasiswa")
    print("[5] Cari Mahasiswa")
    print("[0] Exit")
    print("-"*64)
    selected_menu = input("Pilih menu> ")
    
    if(selected_menu == "1"):
        show_mahasiswa()
    elif(selected_menu == "2"):
        create_mahasiswa()
    elif(selected_menu == "3"):
        edit_mahasiswa()
    elif(selected_menu == "4"):
        delete_mahasiswa()
    elif(selected_menu == "5"):
        search_concat()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_mahasiswa():
    clear_screen()
    mahasiswas = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            mahasiswas.append(row)

    if (len(mahasiswas) > 0):
        labels = mahasiswas.pop(0)
        print(f"{labels[0]} \t\t\t {labels[1]} \t\t\t {labels[2]}")
        print("-"*64)
        for data in mahasiswas:
            print(f'{data[0]} \t\t {data[1]} \t\t {data[2]}')
    else:
        print("Tidak ada data!")
    back_to_menu()


def create_mahasiswa():
    clear_screen()
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NIM', 'NAMA', 'JURUSAN']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        nim = input("NIM: ")
        nama = input("Nama lengkap: ")
        jurusan = input("Jurusan: ")

        writer.writerow({'NIM': nim, 'NAMA': nama, 'JURUSAN': jurusan})    
    
    back_to_menu()


def search_concat():
    clear_screen()
    mahasiswas = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            mahasiswas.append(row)

    nim = input("Cari berdasrakan NIM> ")

    data_found = []

    # mencari mahasiswa
    indeks = 0
    for data in mahasiswas:
        if (data['NIM'] == nim):
            data_found = mahasiswas[indeks]
            
        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"Nama: {data_found['NAMA']}")
        print(f"Jurusan: {data_found['JURUSAN']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()
    


def edit_mahasiswa():
    clear_screen()
    mahasiswas = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            mahasiswas.append(row)

    print("NIM \t NAMA \t\t JURUSAN")
    print("-"*64)

    for data in mahasiswas:
        print(f"{data['NIM']} \t {data['NAMA']} \t {data['JURUSAN']}")

    print("-"*64)
    nim = input("Pilih NIM> ")
    nama = input("nama baru: ")
    jurusan = input("jurusan baru: ")

    # mencari mahasiswa dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in mahasiswas:
        if (data['NIM'] == nim):
            mahasiswas[indeks]['NAMA'] = nama
            mahasiswas[indeks]['JURUSAN'] = jurusan
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NIM', 'NAMA', 'JURUSAN']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in mahasiswas:
            writer.writerow({'NIM': new_data['NIM'], 'NAMA': new_data['NAMA'], 'JURUSAN': new_data['JURUSAN']}) 

    back_to_menu()



def delete_mahasiswa():
    clear_screen()
    mahasiswas = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            mahasiswas.append(row)

    print("NIM \t NAMA \t\t JURUSAN")
    print("-" * 32)

    for data in mahasiswas:
        print(f"{data['NIM']} \t {data['NAMA']} \t {data['JURUSAN']}")

    print("-"*64)
    nim = input("Hapus NIM> ")

    # mencari mahasiswa dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in mahasiswas:
        if (data['NIM'] == nim):
            mahasiswas.remove(mahasiswas[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NIM', 'NAMA', 'JURUSAN']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in mahasiswas:
            writer.writerow({'NIM': new_data['NIM'], 'NAMA': new_data['NAMA'], 'JURUSAN': new_data['JURUSAN']}) 

    print("Data sudah terhapus")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()