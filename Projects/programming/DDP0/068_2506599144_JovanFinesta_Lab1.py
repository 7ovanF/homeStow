# Program menggambar persegi dengan Loop dan While

# input panjang sisi
pjg_sisi_persegi = int(input('Panjang sisi persegi : '))

# print sisi atas
for i in range(pjg_sisi_persegi):
    print('*', end=' ')
print()

# print sisi kiri & kanan
# karena garis jg akan diprint di sisi atas dan bawah, dikurang 2
for i in range(2, pjg_sisi_persegi):
    k = 3
    print('*', end=' ')
    # kali ini looping dgn while
    while k <= pjg_sisi_persegi:
        print(' ', end=' ')
        k += 1
    print('*', end=' ')
    print()

# print sisi bawah
for i in range(pjg_sisi_persegi):
    print('*', end=' ')
print()



# Bonus
jumlah_persegi = int(input('Jumlah Persegi = '))
pjg_sisi_persegi = int(input('Panjang sisi persegi : '))

# looping per baris (setiap baris terdiri atas sisi atas dan sisi-sisi vertikal)
for n in range(jumlah_persegi):
    # garis atas
    for i in range(jumlah_persegi):
        for k in range(1, pjg_sisi_persegi):
            print('*', end=' ')
        # tambah 1 bintang ekstra di akhir
        if (i + 1) == jumlah_persegi:
            print('*')

    # garis vertikal
    for k in range(2, pjg_sisi_persegi):
        for i in range(jumlah_persegi):
            print('*', end=' ')
            # print spasi
            for l in range(2, pjg_sisi_persegi):
                print(' ', end=' ')    
            # tambah 1 bintang ekstra di akhir
            if (i + 1) == jumlah_persegi:
                print('*')

# tutup baris terakhir dengan garis bawah
for i in range(jumlah_persegi):
    for k in range(1, pjg_sisi_persegi):
        print('*', end=' ')
    # tambah 1 bintang ekstra di akhir
    if (i + 1) == jumlah_persegi:
        print('*')
        