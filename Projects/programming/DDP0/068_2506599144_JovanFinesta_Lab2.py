# Fungsi untuk mengecek apakah dua objek akan saling bertabrakan.
# Rincian argumen:
# - A_pos_x: Koordinat x awal objek pertama
# - A_pos_y: Koordinat y awal objek pertama
# - A_speed_x: Kecepatan objek pertama pada sumbu-x
# - A_speed_y: Kecepatan objek pertama pada sumbu-y
# - B_pos_x: Koordinat x awal objek kedua
# - B_pos_y: Koordinat y awal objek kedua
# - B_speed_x: Kecepatan objek kedua pada sumbu-x
# - B_speed_y: Kecepatan objek kedua pada sumbu-y
###############################################################################
# Fungsi ini sudah lengkap. Kamu hanya perlu menggunakannya dengan benar.
###############################################################################
def check_collision(A_pos_x, A_pos_y, A_speed_x, A_speed_y,
                    B_pos_x, B_pos_y, B_speed_x, B_speed_y):

    if A_pos_x == B_pos_x and A_pos_y == B_pos_y:
        return True

    if A_speed_x == B_speed_x and A_speed_y == B_speed_y:
        return False

    delta_x = B_pos_x - A_pos_x
    delta_y = B_pos_y - A_pos_y
    speed_x = B_speed_x - A_speed_x
    speed_y = B_speed_y - A_speed_y

    if delta_x * speed_y != delta_y * speed_x:
        return False

    return ((delta_x > 0) != (speed_x > 0)) or \
           ((delta_y > 0) != (speed_y > 0))

# Fungsi untuk mengkonversi baris input dari user menjadi data yang bisa
# diproses oleh program.


def parse_input_line(line):
    """Memisahkan string pada simbol '|' menjadi beberapa data objek."""

    parts =  line.split('|')

    nama = parts[0]
    jenis = parts[1]
    bobot = int(parts[2])
    x = int(parts[3])
    y = int(parts[4])
    dx = int(parts[5])
    dy = int(parts[6])

    objek = [nama, jenis, bobot, x, y, dx, dy]
    return objek


def death_ray(power):
    """Melenyapkan benda-benda tertentu dengan kekuatan dahsyat!"""
    return f"dilenyapkan dengan death ray dengan daya {power} megawatt"


def repulsor(force):
    """Menolak benda-benda tertentu dengan repulsor."""
    return f"ditolak dengan repulsor dengan gaya {force} kilonewton"

# Fungsi ini akan dieksekusi ketika script dijalankan.


def main():

    # Input posisi awal kapal.
    print("Posisi kapal COSMIC:")
    ship_x = int(input("x="))
    ship_y = int(input("y="))

    # Input kecepatan awal kapal.
    ship_dx = int(input("Kecepatan kapal COSMIC dalam sumbu-x: "))
    ship_dy = 0  # Karena kapal hanya bergerak searah sumbu-x

    n = int(input("Banyaknya data: "))
    daftar_objek = []

    print(f"Masukkan {n} baris dengan format berikut: ")
    print("nama|jenis|bobot|x|y|dx|dy")

    for i in range(n):
        line = input()
        objek = parse_input_line(line)
        daftar_objek.append(objek)

    print("Penanganan: ")
    for objek in daftar_objek:

        # Ambil data objek
        nama, jenis, bobot, x, y, dx, dy = objek

        will_collide = check_collision(ship_x, ship_y, ship_dx, ship_dy,
                                       x,      y,      dx,      dy)

        daftar_tindakan = []

        # Hitung daftar tindakan yang harus diambil
        if not will_collide:
            daftar_tindakan.append("tidak perlu ditangani")
        elif jenis == "Kinetik":
            k = 4
            gaya = bobot * k
            daftar_tindakan.append(repulsor(gaya))
        elif jenis == "Rudal":
            k = 9
            gaya = bobot * k
            daftar_tindakan.append(repulsor(gaya))
            daftar_tindakan.append("dihancurkan dengan point defense turret")
        elif jenis == "Laser":
            daftar_tindakan.append('dipantulkan dengan energy shield')
        elif jenis in ("Drone", "Kapal Musuh"):
            daftar_tindakan.append('dilumpuhkan dengan EMP')
            if jenis == "Kapal Musuh":
                k = 3000
                gaya = nama.len() * k
                daftar_tindakan.append(repulsor(gaya))
                daftar_tindakan.append('dilewati dengan stealth field')
            else:
                k = 15
                daya = bobot * k
                daftar_tindakan.append(death_ray(daya))
        elif jenis == "Asteroid":
            k = 2
            daya = bobot * k
            daftar_tindakan.append(death_ray(daya))
        elif jenis == "Rongsokan":
            k = 3
            daya = bobot * k
            daftar_tindakan.append(death_ray(daya))
        else: 
            k = 1
            daya = bobot * k
            daftar_tindakan.append(death_ray(daya))

        penanganan =  ", kemudian ".join(daftar_tindakan)

        # Cetak tindakan penanganan
        print(f"{nama} {penanganan}.")


# Jalankan fungsi main jika program dijalankan sebagai script
if __name__ == "__main__":
    main()
