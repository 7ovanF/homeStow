# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Daftar group function: 
# 1. MAIN MENU
# 2. MENU BERANGKAT
# 3. MENU KIRIM PESAN
# 4. MENU BACA PESAN
# 5. MENU LAPORAN PERJALANAN
# 6. AKHIRI PERJALANAN
# 7. MISC
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import math
import time

# MAIN MENU
def main():
    # Ditambahkan error handling: sekarang dapat diimplementasikan dengan mudah karena semua function mengacu pada main() ini, bukan di masing2 function per menu. 
    try:
        print(">>===================================================================<<")
        print("||                                                                   ||")
        print("||      🚀 SELAMAT DATANG DI DEK DEPE'S OUTER SPACE INTERFACE 🚀     ||")
        print("||                                                                   ||")
        print(">>===================================================================<<")

        # inisialisasi variabel2 universal tanpa global
        # ternyata pass & return dictionary nggak berat
        state = {
            # status roket
            'nama_roket' : '',
            'kecepatan_roket' : 0,
            'planet_saat_ini' : 'Bumi',
            'koordinat_x' : 0,
            'koordinat_y' : 0, 
            
            # status perjalanan
            'jarak_tempuh' : 0,
            'durasi_perjalanan' : 0,
            'jarak_planet_dari_bumi' : 0,
            'sudut_planet_dari_bumi' : 0,
            'planet_tujuan' : '',
        }
        # jika menetap: while berhenti, program selesai
        not_menetap = True

        # State inisial roket di-set oleh menu pendaftaran
        state['nama_roket'], state['kecepatan_roket'] = pendaftaran_roket()

        # Output
        print()
        print(bold(f"Roket {state['nama_roket']} berkecepatan {state['kecepatan_roket']} km/s telah didaftarkan."))
        delay(0.4)

        # Setiap kembali ke menu() akan masuk ke dalam loop pemilihan menu
        while not_menetap:
            menu_main(state)
            pilihan_menu = int(input("Masukkan pilihan: "))
            
            # Handle pilihan menu
            if pilihan_menu == 1:
                state = menu_berangkat(state)
            elif pilihan_menu == 2:
                menu_kirim_pesan(state)
            elif pilihan_menu == 3:
                menu_baca_pesan(state)
            elif pilihan_menu == 4:
                menu_laporan_perjalanan(state)
            elif pilihan_menu == 5:
                akhiri_perjalanan(state)
                delay(0.5)
                not_menetap = False
            else:
                warning_menu_invalid()
                continue
    except Exception as e:
        print(red(bold(f"Terjadi kesalahan! {e}")))

def pendaftaran_roket():
    """Memunculkan interface pendaftaran, yang me-return input dari user."""
    print()
    print('============================= Pendaftaran =============================')
    print()

    # Input
    nama_roket = input("Masukkan nama roket: ")
    kecepatan_roket = float(input("Masukkan kecepatan roket (km/s): "))
    
    return nama_roket, kecepatan_roket

def menu_main(state):
    """Menampilkan pilihan-pilihan menu, me-return pilihan yang dipilih."""
    print()
    print('============================= Menu Utama ==============================')
    print()
    print('Lokasi saat ini: ' + bold(state['planet_saat_ini']))
    print()
    print('Menu Utama:')
    print("1. Berangkat")
    print("2. Kirim Pesan")
    print("3. Baca Pesan")
    print("4. Lihat Laporan Perjalanan")
    print("5. Akhiri Perjalanan")

    print()
# END MAIN MENU

# MENU BERANGKAT
def menu_berangkat(state):
    """Menampilkan pilihan-pilihan pemberangkatan dan menghandle pilihan-pilihan submenu, lalu me-return state roket yang berubah."""
    while True:
        print()
        print('============================== Berangkat ==============================')
        print()
        print("Pilih opsi navigasi:")
        print("1. Koordinat Kartesian (x, y)")
        print("2. Koordinat Polar (sudut, jarak)")
        print("3. Kembali ke menu utama")
        pilihan_berangkat = int(input("Masukkan pilihan: "))
        if pilihan_berangkat == 1:
            state = berangkat_koordinat_kartesian(state)
            break
        elif pilihan_berangkat == 2:
            state = berangkat_koordinat_polar(state)
            break
        elif pilihan_berangkat == 3:
            break
        else:
            warning_menu_invalid()
            continue
    return state

def berangkat_koordinat_kartesian(state):
    """Berangkat menggunakan input koordinat kartesian, lalu menghitung state-state roket (e.g. jarak tempuh, durasi, dll)."""

    koordinat_x_sebelumnya = state['koordinat_x']
    koordinat_y_sebelumnya = state['koordinat_y']

    state['planet_tujuan'] = input("Masukkan nama planet tujuan: ")
    state['koordinat_x'] = float(input("Masukkan koordinat x dari planet tujuan: "))
    state['koordinat_y'] = float(input("Masukkan koordinat y dari planet tujuan: "))

    # Perhitungan jarak, durasi perjalanan, dll
    perpindahan_x = state['koordinat_x'] - koordinat_x_sebelumnya
    perpindahan_y = state['koordinat_y'] - koordinat_y_sebelumnya
    state['jarak_tempuh'] = math.sqrt((perpindahan_x ** 2) + (perpindahan_y ** 2))
    state['jarak_planet_dari_bumi'] = math.sqrt((state['koordinat_x'] ** 2) + (state['koordinat_y'] ** 2))
    state['durasi_perjalanan'] = state['jarak_tempuh'] / state['kecepatan_roket']
    state['sudut_planet_dari_bumi'] = math.degrees(math.atan2(state['koordinat_y'], state['koordinat_x']))

    # Berangkat ke planet tujuan, lalu kembali ke menu utama
    state = depart(state)
    return state

def berangkat_koordinat_polar(state):
    """Berangkat menggunakan input koordinat polar, lalu menghitung state-state roket (e.g. jarak tempuh, durasi, dll)."""

    state['planet_tujuan'] = input("Masukkan nama planet tujuan: ")
    sudut_dari_planet_saat_ini = float(input("Masukkan sudut terhadap planet tujuan (dalam derajat): "))
    state['jarak_tempuh'] = float(input("Masukkan jarak ke planet tujuan (dalam km): "))

    # Perhitungan jarak, durasi perjalanan, dll
    perpindahan_x = math.cos(math.radians(sudut_dari_planet_saat_ini)) * state['jarak_tempuh']
    perpindahan_y = math.sin(math.radians(sudut_dari_planet_saat_ini)) * state['jarak_tempuh']
    state['koordinat_x'] += perpindahan_x
    state['koordinat_y'] += perpindahan_y
    state['jarak_planet_dari_bumi'] = math.sqrt((state['koordinat_x'] ** 2) + (state['koordinat_y'] ** 2))
    state['durasi_perjalanan'] = state['jarak_tempuh'] / state['kecepatan_roket']
    state['sudut_planet_dari_bumi'] = math.degrees(math.atan2(state['koordinat_y'], state['koordinat_x']))

    # Berangkat ke planet tujuan, lalu kembali ke menu utama
    state = depart(state)
    return state

def depart(state):
    """Melakukan perjalanan, lalu mengupdate planet lokasi."""
    print()
    print('Berangkat!')
    print(20 * '🚀 ')
    print()

    delay(1)

    state['planet_saat_ini'] = state['planet_tujuan']
    state['planet_tujuan'] = ''
    print('✅ Berhasil mendarat di Planet ' + bold(state['planet_saat_ini']))

    delay(0.5)
    return state
# END MENU BERANGKAT

# MENU KIRIM PESAN
def menu_kirim_pesan(state):
    """Menampilkan pilihan-pilihan enkripsi pesan dan menghandle pilihan-pilihan submenu."""
    while True:
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
        # Kembali ke menu utama
        if pilihan_enkripsi == 6:
            break
        # Jika di luar range, pilih ulang
        elif pilihan_enkripsi < 1 or pilihan_enkripsi > 6:
            warning_menu_invalid()
            continue
        isi_pesan_dikirim(state, pilihan_enkripsi)
        break

def isi_pesan_dikirim(state, pilihan_enkripsi):
    """Memunculkan prompt input pesan, lalu melakukan enkripsi pesan sesuai dengan pilihan enkripsi.""" 
    
    while True:
        pesan_unencrypted = input("Masukkan pesan yang ingin dikirim: ")
        pesan_encrypted = ''
        if pilihan_enkripsi == 1:
            pesan_encrypted = encrypt_jarak_tempuh(pesan_unencrypted, state)
        elif pilihan_enkripsi == 2:
            pesan_encrypted = encrypt_nama_planet_saat_ini(pesan_unencrypted, state)
        elif pilihan_enkripsi == 3:
            pesan_encrypted = encrypt_biner(pesan_unencrypted)
        elif pilihan_enkripsi == 4:
            pesan_encrypted = encrypt_heksadesimal(pesan_unencrypted)
        elif pilihan_enkripsi == 5:
            pesan_encrypted = encrypt_membalik(pesan_unencrypted)

        # Jika terjadi masalah (karakter invalid), lakukan input kembali
        if pesan_encrypted is False:
            continue

        print()
        print('Hasil Enkripsi: ' + bold(pesan_encrypted)) 
        delay(1.5)
        break

def encrypt_jarak_tempuh(pesan_unencrypted, state):
    """Enkripsi dengan Caesar Cipher: pindah alfabet berdasarkan jarak tempuh"""
    # digunakan int agar didapat order karakter yg valid 
    jarak_tempuh_floored = math.floor(state['jarak_tempuh'])
    pesan_encrypted = ''
    for i in range(len(pesan_unencrypted)):
        char = pesan_unencrypted[i]
        # Translasi karakter ke urutan integernya (jika invalid, minta input kembali)
        n = translate_to_ord_encrypt(char)
        if n is False:
            return False
        
        # geser karakter
        n += jarak_tempuh_floored
        
        # agar tidak di luar range karakter
        VALID_CHARS = 95
        n = n % VALID_CHARS

        pesan_encrypted += chr(n + 32)
        
    return pesan_encrypted

def encrypt_nama_planet_saat_ini(pesan_unencrypted, state):
    """Enkripsi dengan Vignere Cipher (note: teks menjadi key, sementara nama planet menjadi subjek)"""
    pesan_encrypted = ''
    for i in range(len(pesan_unencrypted)):
        raw_key = pesan_unencrypted[i]

        # Translasi key ke urutan integernya (jika invalid, minta input kembali)
        key = translate_to_ord_encrypt(raw_key)
        if key is False:
            return False

        for char in state['planet_saat_ini']:
            # Translasi karakter ke urutan integernya (jika invalid, minta input kembali)
            n = translate_to_ord_encrypt(char)
            if n is False:
                return False 

            # geser karakter
            n += key
            
            # agar tidak di luar range karakter
            VALID_CHARS = 95
            n = n % VALID_CHARS

            pesan_encrypted += chr(n + 32)
        
    return pesan_encrypted

def encrypt_biner(pesan_unencrypted):
    """Enkripsi ke biner (32 karakter pertama dihapus dari tabel karakter)"""
    pesan_encrypted = ''
    for i in range(len(pesan_unencrypted)):
        char = pesan_unencrypted[i]
        
        # Translasi key ke urutan integernya (jika invalid, minta input kembali)
        n = translate_to_ord_encrypt(char)
        if n is False:
            return False

        byte = ''
        for j in range(7, -1, -1):
            weight = 2 ** j
            bit = math.floor(n / weight)
            byte += str(bit)
            n = n % weight
        pesan_encrypted += byte
    return pesan_encrypted

def encrypt_heksadesimal(pesan_unencrypted):
    """Enkripsi ke heksadesimal (32 karakter pertama dihapus dari tabel karakter)"""
    pesan_encrypted = ''
    for i in range(len(pesan_unencrypted)):
        char = pesan_unencrypted[i]
        
        # Translasi key ke urutan integernya (jika invalid, minta input kembali)
        n = translate_to_ord_encrypt(char)
        if n is False:
            return False
        
        hexa = ''
        for j in range(1, -1, -1):
            weight = 16 ** j
            nib_raw = math.floor(n / weight)
            if nib_raw >= 10:
                nib_raw -= 10
                captl_a_charctr_ordr = 65
                nib = chr(nib_raw + captl_a_charctr_ordr)
            else:
                nib = nib_raw
            hexa += str(nib)
            n = n % weight
        pesan_encrypted += hexa
    return pesan_encrypted

def encrypt_membalik(pesan_unencrypted):
    """Alfabet dibalik dari akhir ke awal"""

    pesan_encrypted = pesan_unencrypted[::-1]
    return pesan_encrypted
# END MENU KIRIM PESAN

# MENU BACA PESAN
def menu_baca_pesan(state):
    """Menampilkan pilihan-pilihan dekripsi pesan dan menghandle pilihan-pilihan submenu."""
    
    while True:
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
        # Kembali ke menu utama
        if pilihan_dekripsi == 6:
            break
        # Jika di luar range, pilih ulang
        elif pilihan_dekripsi < 1 or pilihan_dekripsi > 6:
            warning_menu_invalid()
            continue
        isi_pesan_diterima(state, pilihan_dekripsi)
        break

def isi_pesan_diterima(state, pilihan_dekripsi):
    """Memunculkan prompt input pesan, lalu melakukan dekripsi pesan sesuai dengan pilihan dekripsi.""" 

    while True:
        pesan_undecrypted = input("Masukkan pesan terenkripsi yang ingin dibaca: ")
        pesan_decrypted = ''
        if pilihan_dekripsi == 1:
            pesan_decrypted = decrypt_jarak_tempuh(pesan_undecrypted, state)
        elif pilihan_dekripsi == 2:
            pesan_decrypted = decrypt_nama_planet_saat_ini(pesan_undecrypted, state)
        elif pilihan_dekripsi == 3:
            pesan_decrypted = decrypt_biner(pesan_undecrypted)
        elif pilihan_dekripsi == 4:
            pesan_decrypted = decrypt_heksadesimal(pesan_undecrypted)
        elif pilihan_dekripsi == 5:
            pesan_decrypted = decrypt_membalik(pesan_undecrypted)
    
        # Jika terjadi masalah (karakter invalid), lakukan input kembali
        if pesan_decrypted is False:
            continue

        print()
        print('Hasil Dekripsi: ' + bold(pesan_decrypted)) 
        delay(1.5)
        break

def decrypt_jarak_tempuh(pesan_undecrypted, state):
    """Dekripsi dengan Caesar Cipher: pindah alfabet berdasarkan jarak tempuh"""
    
    jarak_tempuh_floored = math.floor(state['jarak_tempuh'])
    pesan_decrypted = ''
    for i in range(len(pesan_undecrypted)):
        char = pesan_undecrypted[i]

        # Translasi karakter ke urutan integernya (jika invalid, minta input kembali)
        n = translate_to_ord_decrypt(char)
        if n is False:
            return False
        
        # geser karakter
        n -= jarak_tempuh_floored
        
        # agar tidak di luar range karakter
        VALID_CHARS = 95
        n = n % VALID_CHARS

        pesan_decrypted += chr(n + 32)
        
    return pesan_decrypted

def decrypt_nama_planet_saat_ini(pesan_undecrypted, state):
    """Dekripsi dengan Vignere Cipher (note: teks menjadi key, sementara nama planet menjadi subjek)"""
    
    pesan_decrypted = ''
    for i in range(0, len(pesan_undecrypted), len(state['planet_saat_ini'])):
        # cari key dengan membandingkan perbedaan antara huruf pertama kata terenkripsi dan kata terdekripsi saja
        encrypted_char = pesan_undecrypted[i]

        # Translasi karakter ke urutan integernya (jika invalid, minta input kembali)
        encrypted_n = translate_to_ord_decrypt(encrypted_char)
        if encrypted_n is False:
            return False
        
        planet_char = state['planet_saat_ini'][0]

        planet_n = translate_to_ord_decrypt(planet_char)
        if planet_n is False:
            return False
        
        key = (encrypted_n - planet_n) % 95
        
        raw_key = chr(key + 32)
        pesan_decrypted += raw_key
        
    return pesan_decrypted
    
def decrypt_biner(pesan_undecrypted):
    """Dekripsi dari biner (32 karakter pertama dihapus dari tabel karakter)"""

    pesan_decrypted = ''
    for i in range(0, len(pesan_undecrypted), 8):
        byte = pesan_undecrypted[i:i+8]
        n = 0
        for m in range(len(byte)):
            j = 7 - m
            weight = 2 ** j
            bit = byte[m]
            n += weight * int(bit)
        pesan_decrypted += chr(n + 32)
    return pesan_decrypted

def decrypt_heksadesimal(pesan_undecrypted):
    """Dekripsi dari heksadesimal (32 karakter pertama dihapus dari tabel karakter)"""
    pesan_decrypted = ''
    for i in range(0, len(pesan_undecrypted), 2):
        byte = pesan_undecrypted[i:i+2]
        n = 0
        for m in range(len(byte)):
            j = 1 - m
            weight = 16 ** j
            nib = byte[m]
            if nib >= 'A' and nib <= 'F':
                nib_raw = ord(nib) - ord('A') + 10
            else:
                nib_raw = int(nib)
            
            n += int(nib_raw) * weight
        pesan_decrypted += chr(n + 32)
    return pesan_decrypted

def decrypt_membalik(pesan_undecrypted):
    """Alfabet dibalik dari akhir ke awal"""
    
    pesan_decrypted = pesan_undecrypted[::-1]
    return pesan_decrypted
# END MENU BACA PESAN

# MENU LAPORAN PERJALANAN
def menu_laporan_perjalanan(state):
    """Menampilkan laporan perjalanan."""
    print()
    print('========================= Laporan Perjalanan ==========================')
    print()
    print('Nama Roket: ' + bold(state['nama_roket']))
    print('Kecepatan Roket: ' + bold(state['kecepatan_roket']) + ' km/s')
    print('Jarak Tempuh: ' + bold(state['jarak_tempuh']) + ' km')
    print('Durasi Perjalanan: ' + bold(state['durasi_perjalanan']) + ' detik')
    print()
    print('====================== Informasi Lokasi Saat Ini ======================')
    print()
    print('Planet Saat Ini: ' + bold(state['planet_saat_ini']))
    print('Jarak Planet dari Bumi: ' + bold(state['jarak_planet_dari_bumi']) + ' km')
    print('Sudut Planet dari Bumi: ' + bold(state['sudut_planet_dari_bumi']) + ' derajat')
    print()
    input_keluar = input("Tekan 'ENTER' untuk keluar dari menu laporan. ")
# END MENU LAPORAN PERJALANAN

# AKHIRI PERJALANAN
def akhiri_perjalanan(state):
    """Mengakhiri perjalanan. Selamat menetap!"""
    print()
    print('========================== Akhiri Perjalanan ==========================')
    print()
    print('Selamat menetap di planet ' + bold(state['planet_saat_ini']))
    print()
    print('=======================================================================')
# END AKHIRI PERJALANAN

# MISC
def warning_menu_invalid():
    """Warning / pesan error ketika pilihan menu di luar range."""
    print()
    print(bold(red("Mohon pilih opsi yang valid.")))  
    delay(0.4)
    

def translate_to_ord_encrypt(char):
    """Mengubah sebuah karakter ke integer berdasarkan urutan karakternya, lalu menghilangkan karakter-karakter unprintable (NUL, \\t, etc) (Khusus enkripsi)""" 
    MISSING_CHARS = 32

    o = ord(char)
    n = o - MISSING_CHARS # minus 32, sesuai dgn tabel
    validasi = validasi_karakter_enkripsi(n, char)
    if validasi:
        return n
    else:
        return False

def validasi_karakter_enkripsi(n, char):
    """Validasi jika karakter hasil enkripsi di luar tabel karakter. Jika ya, tampilkan pesan error.""" 
    VALID_CHAR_RANGE = 94

    if n < 0 or n > VALID_CHAR_RANGE:
        print(red(f'Karakter "{char}" tidak dapat dienkripsi...'))
        return False
    else:
        return True

# (Saya pisah biar messagenya beda aja)
def translate_to_ord_decrypt(char):
    """Mengubah sebuah karakter ke integer berdasarkan urutan karakternya, lalu menghilangkan karakter-karakter unprintable (NUL, \\t, etc) (Khusus dekripsi)""" 
    MISSING_CHARS = 32

    o = ord(char)
    n = o - MISSING_CHARS # minus 32, sesuai dgn tabel
    validasi = validasi_karakter_dekripsi(n, char)
    if validasi:
        return n
    else:
        return False

def validasi_karakter_dekripsi(n, char):
    """Validasi jika karakter hasil dekripsi di luar tabel karakter. Jika ya, tampilkan pesan error."""
    VALID_CHAR_RANGE = 94

    if n < 0 or n > VALID_CHAR_RANGE:
        print(red(f'Karakter "{char}" tidak dapat didekripsi...'))
        return False
    else:
        return True


def bold(text):
    """bikin bold"""
    return f"\033[1m{text}\033[0m"

def red(text):
    """bikin merah"""
    return f"\033[31m{text}\033[0m"

def delay(delay_time):
    """bikin delay"""
    time.sleep(delay_time)
# END MISC

# LAUNCH
if __name__ == '__main__':
    main()