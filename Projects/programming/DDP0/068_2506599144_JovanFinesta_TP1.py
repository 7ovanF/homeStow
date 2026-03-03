import math
import time

# inisialisasi variabel
# Kesalahan: penggunaan global variable berlebih -> menimbulkan clutter / spaghetti, segala bentuk kebingungan.
# Best practice: Class (walau itu sudah masuk ranah OOP) atau apapun yg bukan global
nama_roket = ''
kecepatan_roket = 0
jarak_tempuh = 0
durasi_perjalanan = 0

planet_saat_ini = 'Bumi'
koordinat_x = 0
koordinat_y = 0
jarak_planet_dari_bumi = 0
sudut_planet_dari_bumi = 0
planet_tujuan = ''

pilihan_enkripsi = 0
pilihan_dekripsi = 0


# MAIN MENU
def main():
    # Kesalahan 2: print dalam function
    # - Sebuah function idealnya hanya melakukan 1 task
    # # -> Single Responsibility / Separation of Concerns (contoh: generate string doang, bukan generate DAN print)
    # - testing jadi lebih kompleks
    # - tidak re-usable
    # Best Practice: return string, print di luar def
    print(""">>===================================================================<<
||                                                                   ||
||      🚀 SELAMAT DATANG DI DEK DEPE'S OUTER SPACE INTERFACE 🚀     ||
||                                                                   ||
>>===================================================================<<
""")
    pendaftaran_roket()

def pendaftaran_roket():
    print()
    print('============================= Pendaftaran =============================')
    print()

    # Input
    global nama_roket, kecepatan_roket
    nama_roket = input("Masukkan nama roket: ")
    kecepatan_roket = float(input("Masukkan kecepatan roket (km/s): "))
    
    # Output
    print()
    print(bold(f"Roket {nama_roket} berkecepatan {kecepatan_roket} km/s telah didaftarkan."))
    delay(0.4)

    menu_main()

def menu_main():
    print()
    print('============================= Menu Utama ==============================')
    print()
    print('Lokasi saat ini: ' + bold(planet_saat_ini))
    print()
    print('Menu Utama:')
    print("1. Berangkat")
    print("2. Kirim Pesan")
    print("3. Baca Pesan")
    print("4. Lihat Laporan Perjalanan")
    print("5. Akhiri Perjalanan")

    print()
    pilihan_menu = int(input("Masukkan pilihan: "))
    if pilihan_menu == 1:
        menu_berangkat()
    elif pilihan_menu == 2:
        menu_kirim_pesan()
    elif pilihan_menu == 3:
        menu_baca_pesan()
    elif pilihan_menu == 4:
        menu_laporan_perjalanan()
    elif pilihan_menu == 5:
        akhiri_perjalanan()
    else:
        warning_menu_invalid()
        menu_main()
# END MAIN MENU

# MENU BERANGKAT
def menu_berangkat():
    print()
    print('============================== Berangkat ==============================')
    print()
    print("Pilih opsi navigasi:")
    print("1. Koordinat Kartesian (x, y)")
    print("2. Koordinat Polar (sudut, jarak)")
    print("3. Kembali ke menu utama")
    pilihan_berangkat = int(input("Masukkan pilihan: "))
    if pilihan_berangkat == 1:
        berangkat_koordinat_kartesian()
    elif pilihan_berangkat == 2:
        berangkat_koordinat_polar()
    elif pilihan_berangkat == 3:
        menu_main()
    else:
        warning_menu_invalid()
        menu_berangkat()

def berangkat_koordinat_kartesian():
    global planet_tujuan, koordinat_x, koordinat_y, jarak_tempuh, durasi_perjalanan, jarak_planet_dari_bumi, sudut_planet_dari_bumi, kecepatan_roket

    koordinat_x_sebelumnya = koordinat_x
    koordinat_y_sebelumnya = koordinat_y

    planet_tujuan = input("Masukkan nama planet tujuan: ")
    koordinat_x = float(input("Masukkan koordinat x dari planet tujuan: "))
    koordinat_y = float(input("Masukkan koordinat y dari planet tujuan: "))

    # Perhitungan jarak, durasi perjalanan, dll
    perpindahan_x = koordinat_x - koordinat_x_sebelumnya
    perpindahan_y = koordinat_y - koordinat_y_sebelumnya
    jarak_tempuh = math.sqrt((perpindahan_x ** 2) + (perpindahan_y ** 2))
    jarak_planet_dari_bumi = math.sqrt((koordinat_x ** 2) + (koordinat_y ** 2))
    durasi_perjalanan = jarak_tempuh / kecepatan_roket
    sudut_planet_dari_bumi = math.degrees(math.atan2(koordinat_y, koordinat_x))

    # Berangkat ke planet tujuan, lalu kembali ke menu utama
    depart()
    menu_main()

def berangkat_koordinat_polar():
    global planet_tujuan, koordinat_x, koordinat_y, jarak_tempuh, durasi_perjalanan, jarak_planet_dari_bumi, sudut_planet_dari_bumi, kecepatan_roket

    planet_tujuan = input("Masukkan nama planet tujuan: ")
    sudut_planet_dari_bumi = float(input("Masukkan sudut terhadap planet tujuan (dalam derajat): "))
    jarak_tempuh = float(input("Masukkan jarak ke planet tujuan (dalam km): "))

    # Perhitungan jarak, durasi perjalanan, dll
    perpindahan_x = math.cos(math.radians(sudut_planet_dari_bumi)) * jarak_tempuh
    perpindahan_y = math.sin(math.radians(sudut_planet_dari_bumi)) * jarak_tempuh
    koordinat_x = perpindahan_x + koordinat_x
    koordinat_y = perpindahan_y + koordinat_y
    jarak_planet_dari_bumi = math.sqrt((koordinat_x ** 2) + (koordinat_y ** 2))
    durasi_perjalanan = jarak_tempuh / kecepatan_roket

    # Berangkat ke planet tujuan, lalu kembali ke menu utama
    depart()
    menu_main()
# END MENU BERANGKAT

# MENU KIRIM PESAN
def menu_kirim_pesan():
    global pilihan_enkripsi
    print()
    print('========================= Kirim Pesan Ke Bumi =========================')
    print()
    print("Metode Enkripsi:")
    print("1. Enkripsi berdasarkan Jarak Tempuh")
    print("2. Enkripsi berdasarkan Nama Planet Saat Ini")
    print("3. Enkripsi Biner")
    print("4. Enkripsi Heksadesimal")
    print("5. Enkripsi Membalik")
    print("6. Kembali ke Menu Utama")
    pilihan_enkripsi = int(input("Masukkan pilihan: "))
    if (pilihan_enkripsi == 6):
        menu_main()
    elif pilihan_enkripsi < 1 or pilihan_enkripsi > 6:
        warning_menu_invalid()
        menu_kirim_pesan()
    isi_pesan_dikirim()

def isi_pesan_dikirim():
    global pilihan_enkripsi
    pesan_unencrypted = input("Masukkan pesan yang ingin dikirim: ")
    pesan_encrypted = ''
    if pilihan_enkripsi == 1:
        pesan_encrypted = encrypt_jarak_tempuh(pesan_unencrypted)
    elif pilihan_enkripsi == 2:
        pesan_encrypted = encrypt_nama_planet_saat_ini(pesan_unencrypted)
    elif pilihan_enkripsi == 3:
        pesan_encrypted = encrypt_biner(pesan_unencrypted)
    elif pilihan_enkripsi == 4:
        pesan_encrypted = encrypt_heksadesimal(pesan_unencrypted)
    elif pilihan_enkripsi == 5:
        pesan_encrypted = encrypt_membalik(pesan_unencrypted)
    
    print()
    print('Hasil Enkripsi: ' + bold(pesan_encrypted)) 
    delay(1.5)
    menu_main()

# apakah tidak ada larangan utk ord() hehe
def encrypt_jarak_tempuh(pesan_unencrypted):
    # Caesar Cipher: pindah alfabet berdasarkan jarak tempuh
    global jarak_tempuh
    jarak_tempuh_floored = math.floor(jarak_tempuh)
    pesan_encrypted = ''
    for i in range(len(pesan_unencrypted)):
        char = pesan_unencrypted[i]
        n = translate_to_ord_encrypt(char)
        # geser karakter
        n += jarak_tempuh_floored
        # agar tidak di luar range karakter
        n = n % 95

        pesan_encrypted += chr(n + 32)
        
    return pesan_encrypted

def encrypt_nama_planet_saat_ini(pesan_unencrypted):
    # Vignere Cipher (note: teks menjadi key, sementara nama planet menjadi subjek)
    global planet_saat_ini
    pesan_encrypted = ''
    for i in range(len(pesan_unencrypted)):
        raw_key = pesan_unencrypted[i]
        key = translate_to_ord_encrypt(raw_key) 
        for j in range(len(planet_saat_ini)):
            char = planet_saat_ini[j]
            n = translate_to_ord_encrypt(char) 
            n += key
            # agar tidak di luar range karakter
            n = n % 95
            pesan_encrypted += chr(n + 32)
        
    return pesan_encrypted
    

def encrypt_biner(pesan_unencrypted):
    pesan_encrypted = ''
    for i in range(len(pesan_unencrypted)):
        char = pesan_unencrypted[i]
        n = translate_to_ord_encrypt(char) 

        byte = ''
        for j in range(7, -1, -1):
            const = 2 ** j
            bit = math.floor(n / const)
            byte += str(bit)
            n = n % const
        pesan_encrypted += byte
    return pesan_encrypted

def encrypt_heksadesimal(pesan_unencrypted):
    pesan_encrypted = ''
    for i in range(len(pesan_unencrypted)):
        char = pesan_unencrypted[i]
        n = translate_to_ord_encrypt(char) 
        hexa = ''
        for j in range(1, -1, -1):
            const = 16 ** j
            nib_raw = math.floor(n / const)
            if nib_raw >= 10:
                nib_raw -= 10
                captl_a_charctr_ordr = 65
                # semoga chr() jg dibolehin
                nib = chr(nib_raw + captl_a_charctr_ordr)
            else:
                nib = nib_raw
            hexa += str(nib)
            n = n % const
        pesan_encrypted += hexa
    return pesan_encrypted

def encrypt_membalik(pesan_unencrypted):
    # Alfabet dibalik dari akhir ke awal
    pesan_encrypted = ''
    # # Ide pertama saya yaitu memakai [] tapi bukannya itu kehitung sbg .index() ya (ilegal)
    # for i in range(len(pesan_unencrypted) - 1, -1, -1):
    #     pesan_encrypted += pesan_unencrypted[i]

    # Akhirnya saya nanya google (gmn saya tau slicing itu apaan ;-;)
    pesan_encrypted = pesan_unencrypted[::-1]
    return pesan_encrypted

# END MENU KIRIM PESAN

# MENU BACA PESAN
def menu_baca_pesan():
    global pilihan_dekripsi
    print()
    print('============================= Baca Pesan ==============================')
    print()
    print("Metode Dekripsi:")
    print("1. Dekripsi berdasarkan Jarak Tempuh")
    print("2. Dekripsi berdasarkan Nama Planet Saat Ini")
    print("3. Dekripsi Biner")
    print("4. Dekripsi Heksadesimal")
    print("5. Dekripsi Membalik")
    # print("6. Dekripsi Brute Force (Jarak Tempuh)")
    # print("7. Dekripsi Brute Force (Nama Planet)")
    print("6. Kembali ke Menu Utama")
    pilihan_dekripsi = int(input("Masukkan pilihan: "))
    if (pilihan_dekripsi == 6):
        menu_main()
    elif pilihan_dekripsi < 1 or pilihan_dekripsi > 6:
        warning_menu_invalid()
        menu_baca_pesan()
    isi_pesan_diterima()

def isi_pesan_diterima():
    global pilihan_dekripsi
    pesan_undecrypted = input("Masukkan pesan terenkripsi yang ingin dibaca: ")
    pesan_decrypted = ''
    if pilihan_dekripsi == 1:
        pesan_decrypted = decrypt_jarak_tempuh(pesan_undecrypted)
    elif pilihan_dekripsi == 2:
        pesan_decrypted = decrypt_nama_planet_saat_ini(pesan_undecrypted)
    elif pilihan_dekripsi == 3:
        pesan_decrypted = decrypt_biner(pesan_undecrypted)
    elif pilihan_dekripsi == 4:
        pesan_decrypted = decrypt_heksadesimal(pesan_undecrypted)
    elif pilihan_dekripsi == 5:
        pesan_decrypted = decrypt_membalik(pesan_undecrypted)
    
    print()
    print('Hasil Enkripsi: ' + bold(pesan_decrypted)) 
    delay(1.5)
    menu_main()

# apakah tidak ada larangan utk ord() hehe
def decrypt_jarak_tempuh(pesan_undecrypted):
    # Caesar Cipher: pindah alfabet berdasarkan jarak tempuh
    global jarak_tempuh
    jarak_tempuh_floored = math.floor(jarak_tempuh)
    pesan_decrypted = ''
    for i in range(len(pesan_undecrypted)):
        char = pesan_undecrypted[i]
        n = translate_to_ord_decrypt(char)
        # geser karakter
        n -= jarak_tempuh_floored
        # agar tidak di luar range karakter
        n = n % 95

        pesan_decrypted += chr(n + 32)
        
    return pesan_decrypted

def decrypt_nama_planet_saat_ini(pesan_undecrypted):
    # Vignere Cipher (note: teks menjadi key, sementara nama planet menjadi subjek)
    global planet_saat_ini
    pesan_decrypted = ''
    for i in range(0, len(pesan_undecrypted), len(planet_saat_ini)):
        # cari key dengan membandingkan perbedaan antara huruf pertama terenkripsi dan terdekripsi saja
        encrypted_char = pesan_undecrypted[i]
        encrypted_n = translate_to_ord_decrypt(encrypted_char)
        
        planet_char = planet_saat_ini[0]
        planet_n = translate_to_ord_decrypt(planet_char)
        
        key = (encrypted_n - planet_n) % 95
        
        raw_key = chr(key + 32)
        pesan_decrypted += raw_key
        
    return pesan_decrypted
    
def decrypt_biner(pesan_undecrypted):
    pesan_decrypted = ''
    for i in range(0, len(pesan_undecrypted), 8):
        byte = pesan_undecrypted[i:i+8]
        n = 0
        for m in range(len(byte)):
            j = 7 - m
            const = 2 ** j
            bit = byte[m]
            n += const * int(bit)
            
        pesan_decrypted += chr(n + 32)
    return pesan_decrypted

def decrypt_heksadesimal(pesan_undecrypted):
    pesan_decrypted = ''
    for i in range(0, len(pesan_undecrypted), 2):
        byte = pesan_undecrypted[i:i+2]
        n = 0
        for m in range(len(byte)):
            j = 1 - m
            const = 16 ** j
            nib = byte[m]
            if nib >= 'A' and nib <= 'F':
                nib_raw = ord(nib) - ord('A') + 10
            else:
                nib_raw = int(nib)
            
            n += int(nib_raw) * const
        pesan_decrypted += chr(n + 32)
    return pesan_decrypted

def decrypt_membalik(pesan_undecrypted):
    # Alfabet dibalik dari akhir ke awal
    pesan_decrypted = ''
    
    pesan_decrypted = pesan_undecrypted[::-1]
    return pesan_decrypted

# END MENU BACA PESAN

# MENU LAPORAN PERJALANAN
def menu_laporan_perjalanan():
    global nama_roket, kecepatan_roket, jarak_tempuh, durasi_perjalanan, planet_saat_ini, jarak_planet_dari_bumi, sudut_planet_dari_bumi
    print()
    print('========================= Laporan Perjalanan ==========================')
    print()
    print('Nama Roket: ' + bold(nama_roket))
    print('Kecepatan Roket: ' + bold(kecepatan_roket) + ' km/s')
    print('Jarak Tempuh: ' + bold(jarak_tempuh) + ' km')
    print('Durasi Perjalanan: ' + bold(durasi_perjalanan) + ' detik')
    print()
    print('====================== Informasi Lokasi Saat Ini ======================')
    print()
    print('Planet Saat Ini: ' + bold(planet_saat_ini))
    print('Jarak Planet dari Bumi: ' + bold(jarak_planet_dari_bumi) + ' km')
    print('Sudut Planet dari Bumi: ' + bold(sudut_planet_dari_bumi) + ' derajat')
    print()
    input_keluar = input("Tekan 'ENTER' untuk keluar dari menu laporan. ")
    menu_main()
# END MENU LAPORAN PERJALANAN

# AKHIRI PERJALANAN
def akhiri_perjalanan():
    print()
    print('========================== Akhiri Perjalanan ==========================')
    print()
    print('Selamat menetap di planet ' + bold(planet_saat_ini))
    print()
    print('=======================================================================')
# END AKHIRI PERJALANAN

# MISC
def warning_menu_invalid():
    print()
    print(bold(red("Mohon pilih opsi yang valid.")))  
    delay(0.4)

def depart():
    global planet_tujuan, planet_saat_ini
    print()
    print('Berangkat!')
    print(20 * '🚀 ')
    print()
    delay(1)
    planet_saat_ini = planet_tujuan
    planet_tujuan = ''
    print('✅ Berhasil mendarat di Planet ' + bold(planet_saat_ini))
    delay(0.5)
    
def translate_to_ord_encrypt(char):
    o = ord(char)
    n = o - 32 # minus 32, sesuai dgn tabel
    validasi_karakter_enkripsi(n, char)
    return n
    
def translate_to_ord_decrypt(char):
    o = ord(char)
    n = o - 32 # minus 32, sesuai dgn tabel
    validasi_karakter_dekripsi(n, char)
    return n

def validasi_karakter_enkripsi(n, char):
    # jika di luar tabel karakter, tampilkan pesan error
    if n < 0 or n > 94:
        print(red(f'Karakter "{char}" tidak dapat dienkripsi...'))
        isi_pesan_dikirim()
    else:
        return

def validasi_karakter_dekripsi(n, char):
    # jika di luar tabel karakter, tampilkan pesan error
    if n < 0 or n > 94:
        print(red(f'Karakter "{char}" tidak dapat didekripsi...'))
        isi_pesan_diterima()
    else:
        return


def bold(text):
    return f"\033[1m{text}\033[0m"

def red(text):
    return f"\033[31m{text}\033[0m"

def delay(delay_time):
    time.sleep(delay_time)
# END MISC

# LAUNCH
if __name__ == '__main__':
    main()
