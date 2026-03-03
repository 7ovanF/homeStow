# import math
# import time

# WEEK 0
# print('Hello World!')
# nama_mahasiswa = input('Nama Mahasiswa: ')
# inputangka = input('Masukkan angka: ')
# outputangka = int(inputangka)
# print('Nama anda: ' + nama_mahasiswa)
# print('Angka pilihan anda: ' + outputangka)

# # nama, umur, berat badan, sudah makan belum?
# nama = 'Nama'
# umur = 20
# berat_badan = 60.2
# sudah_makan_belum = True
# print(nama + " " + str(umur) + " " + str(berat_badan) + " " + str(sudah_makan_belum))
# print(True * False)

# import math
# pi = math.pi
# inputRadius = input('Radius/jari-jari lingkaran: ')
# luaslingkaran = int(inputRadius)**2 * pi
# kelilinglingkaran = 2 * int(inputRadius) * pi
# print('Luas : ' + str(luaslingkaran))
# print('Keliling : ' + str(kelilinglingkaran))

# quiz 0
# print()
# print(88 * '-')
# print('Selamat datang di sistem perhitungan Toko Buah Ranarit! Silahkan input harga kedua buah.')
# print(88 * '-')
# print()


# # Input harga buah A dan B
# harga_a = float(input('Masukkan harga buah A (dalam ribuan): '))
# harga_b = float(input('Masukkan harga buah B (dalam ribuan): '))
# # End input


# # Perhitungan

# # (Parse ke float biar bisa dihitung)
# float_harga_a = float(harga_a)
# float_harga_b = float(harga_b)

# jumlah_harga = float_harga_a + float_harga_b
# perkalian_harga = float_harga_a * float_harga_b
# sisa_bagi_a_per_b = float_harga_a % float_harga_b
# jumlah_buah = 2
# int_rata2_harga = round(jumlah_harga / jumlah_buah)
# selisih_harga = abs(float_harga_a - float_harga_b)

# # End perhitungan


# # Pemisah
# print()
# print('------------------')
# print('Hasil Perhitungan')
# print('(dalam ribuan)')
# print('------------------')
# # End pemisah


# # Output
# print('Jumlah harga: ' + str(jumlah_harga))
# print('Perkalian harga: ' + str(perkalian_harga))
# print('Sisa bagi A % B: ' + str(sisa_bagi_a_per_b))
# print('Rata-rata harga: ' + str(int_rata2_harga))
# print('Selisih harga: ' + str(selisih_harga))
# # End output

# print()
# print(87 * '-')
# print('Terima kasih telah berbelanja di Toko Buah Ranarit! Tolong laik, share, dan sabskraib!!')
# print(87 * '-')
# WEEK 1

# a = 200
# b = 201
# if b > a:
#     print('B lebih besar dari A')
# elif b == a:
#     print('B sama dengan A')
# else:
#     print('A lebih besar dari B')

# if b > a or b < a:
#     print('B tidak sama dengan A')

# a = int(input('Masukkan angka A: '))
# b = int(input('Masukkan angka B: '))
# c = int(input('Masukkan angka C: '))
# d = int(input('Masukkan angka D: '))

# angka_terbesar = 0
# if a > b and a > c and a > d:
#     angka_terbesar = a
# elif b > a and b > c and b > d:
#     angka_terbesar = b
# elif c > a and c > b and c > d:
#     angka_terbesar = c
# elif d > a and d > b and d > c:
#     angka_terbesar = d

# print('Angka terbesar adalah ' + str(angka_terbesar))

# i = 1
# while i > 0:
#     print('$$$money generated$$$ :', i)
#     i += 1

# for i in range(4):
#     print(i)
# for i in range(5, 11):
#     print(i)
# for i in range(11, -5, -2):
#     print(i)
# for i in range(0, 21, 2):
#     print(f'angka genap: {i}')

# # mulai dari 0, nambah 1, stop pas 5
# for i in range(10):
#     print(i)
#     if i == 5:
#         break

# # mulai dari 1, skip yg genap
# for i in range(1, 6):
#     if(i % 2 == 0):
#         continue
#     print(i)

# # mulai dari 1, stop sebelum 6, nambah 2 
# for i in range(1,6,2):
#     print(i)

# # mulai dari 1, menambah 2, saat 5 stop
# i = 1
# while i < 11:
#     print(i)
#     if(i == 5):
#         break
#     i += 2

# a = [1,2,3]
# b = [7,8,9]

# for i in a:
#     for j in b:
#         k = i * j
#         print(f'{i} * {j} = {k}')
#     print()

# # Quiz 1

# number = int(input("Masukkan suatu angka: "))
# if number > 5:
#     print("Angka lebih besar dari 5")
# elif number < 5:
#     print("Angka lebih kecil dari 5")
# elif number == 5:
#     print("Angka sama dengan 5")

# # untuk menambah delay
# import time

# angka_countdown = int(input("Masukkan bilangan bulat: "))
# # countdown angka sampai 0
# while angka_countdown > 0:
#     # simpan angka sekarang untuk looping (print sebanyak angka itu sendiri)
#     angka_sekarang = angka_countdown
#     # print angka tersebut sebanyak angka itu sendiri
#     while angka_sekarang > 0:
#         print(angka_countdown, end=" ")
#         angka_sekarang -= 1
#     # extra: delay 1 detik
#     time.sleep(1)
#     print()
#     angka_countdown -= 1
# time.sleep(1)

# # enkripsi test
# char = input()
# # apakah tidak ada larangan utk ord() hehe
# o = ord(char)
# n = o - 32
# if n < 0 or n > 94:
#     print('INVALID CHAR DETECTED...')
# byte = ''
# for j in range(7, -1, -1):
#     const = 2 ** j
#     bit = math.floor(n / const)
#     byte += str(bit)
#     n = n % const
#     print(n, const)
#     # if n >= power:
#     #     byte += '1'
#     #     n = n - power
#     # else:
#     #     byte += '0'
    
# print(byte)

# n = o - 32
# hexa = ''
# for j in range(1, -1, -1):
#     const = 16 ** j
#     nib_raw = math.floor(n / const)
#     if nib_raw >= 10:
#         nib_raw -= 10
#         captl_a_charctr_ordr = 65
#         nib = chr(nib_raw + captl_a_charctr_ordr)
#     else:
#         nib = nib_raw
#     hexa += str(nib)
#     n = n % const
#     print(n, const)
# print(hexa)
    
# byte = [n * 2 ** 7, n * 2 ** 6, n * 2 ** 5, n * 2 ** 4, n * 2 ** 3, n * 2 ** 2, n * 2 ** 1, n * 2 ** 0]


# # Quiz 2
# dataIkan =  [
# ["Ikan Lele", "Clarias batrachus", "Clariidae"],
# ["Ikan Gurame", "Osphronemus goramy", "Osphronemidae"],
# ["Ikan Cupang", "Betta splendens", "Osphronemidae"]]

# def tampilkanIkan(data_ikan):
#     """Function untuk membuat tabel berisi data-data ikan."""

#     tabel_ikan = ''
#     jumlah_ikan = len(data_ikan)

#     # menentukan panjang setiap bagian(biar rata)
#     panjang_label = 15
#     panjang_isi = 25

#     # deklarasi nomor indexing untuk mengambil dari setiap data ikan 
#     index_nama_ikan = 0
#     index_ilmiah_ikan = 1
#     index_family_ikan = 2


#     # Row Nama Ikan
#     label = 'Nama Ikan'
#     tabel_ikan += f'{label:<{panjang_label}}|' # Label

#     for i in range(jumlah_ikan):
#         nama_ikan = data_ikan[i][index_nama_ikan]
#         tabel_ikan += f'{nama_ikan:^{panjang_isi}}'
#         if (i + 1) != jumlah_ikan:
#             tabel_ikan += '|'
            
#     tabel_ikan += '\n' # new line

#     # Row Nama Ilmiah
#     label = 'Nama Ilmiah'
#     tabel_ikan += f'{label:<{panjang_label}}|' # Label

#     for i in range(jumlah_ikan):
#         ilmiah_ikan = data_ikan[i][index_ilmiah_ikan]
#         tabel_ikan += f'{ilmiah_ikan:^{panjang_isi}}'
#         if (i + 1) != jumlah_ikan:
#             tabel_ikan += '|'

#     tabel_ikan += '\n' # new line

#     # Row Nama Genus
#     label = 'Nama Genus'
#     tabel_ikan += f'{label:<{panjang_label}}|' # Label

#     for i in range(jumlah_ikan):
#         ilmiah_ikan = data_ikan[i][index_ilmiah_ikan]
#         genus_ikan = ilmiah_ikan.split(' ')[0]
#         tabel_ikan += f'{genus_ikan:^{panjang_isi}}'
#         if (i + 1) != jumlah_ikan:
#             tabel_ikan += '|'

#     tabel_ikan += '\n' # new line

#     # Row Nama Family
#     label = 'Nama Family'
#     tabel_ikan += f'{label:<{panjang_label}}|' # Label

#     for i in range(jumlah_ikan):
#         family_ikan = data_ikan[i][index_family_ikan]
#         tabel_ikan += f'{family_ikan:^{panjang_isi}}'
#         if (i + 1) != jumlah_ikan:
#             tabel_ikan += '|'

#     return tabel_ikan

# print(tampilkanIkan(dataIkan))

# from math import *

# angka = float(input('angka desimal: '))
# print(f'Pembulatan ke atas: {ceil(angka)}')

# import turtle as t

# for i in range(5):
#     t.forward(100)
#     t.left(72)

# # Program untuk mencari tahu halaman, kolom, dan baris sebuah alamat.
# nomor_entri = int(input("Masukkan nomor entri dari alamat yang dicari = "))
# jumlah_baris = int(input("Masukkan jumlah baris per halaman buku telepon = "))
# jumlah_kolom = int(input("Masukkan jumlah kolom per halaman buku telepon = "))
# entri_per_halaman = jumlah_baris * jumlah_kolom

# # Index entri yang dimulai dari 0
# index_entri = nomor_entri - 1

# # Untuk mencari lokasi:
# ## Halaman
# lokasi_halaman = index_entri // entri_per_halaman + 1
# ## Baris (note: jumlah entri per baris adalah jumlah_kolom)
# lokasi_baris = index_entri % jumlah_baris + 1
# ## Kolom (note: jumlah entri per kolom adalah jumlah_baris)
# lokasi_kolom = index_entri % jumlah_kolom + 1

# # Output hasil pencarian
# print(f"Entri ke-{nomor_entri} berada di halaman {lokasi_halaman}, baris ke-{lokasi_baris}, kolom ke-{lokasi_kolom}")

# # Program handle exception sampai tidak ada error
# while True:
#     try:
#         angka = int(input('masukkan angka: '))
#         print(angka)
#         break
#     except ValueError:
#         print('failed converting')
#     except KeyboardInterrupt:
#         print('end')
#         break
#     except Exception as err:
#         print('Error:', err)

def contains_vowel(word):
    for char in word:
        if char in 'aiueo':
            return True
    return False

with open('input.txt', 'r') as file:
    count = 0
    for line in file:
        for word in line.split():
            if contains_vowel(word):
                count += 1
    print(count)

