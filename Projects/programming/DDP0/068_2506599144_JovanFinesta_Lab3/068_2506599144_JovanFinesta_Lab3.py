import turtle as t
import math
import xml.etree.ElementTree as ET

moving = False
collided = False
cockpit_coor = (345.0, 10.0)
escape_pod_coor = (-250.0, -10.0)
# escape_pod_coor = (300.0, 10.0) # CHEAT
trail: list[tuple[tuple[float, float], tuple[float, float]]] = []
line_list: list[tuple[tuple[float, float], tuple[float, float]]] = []

# Segmen pergerakan
def draw_line(
    point1: tuple[float, float], point2: tuple[float, float], turtle: t.Turtle
) -> None:
    """
    Menggambar garis antar 2 titik
    Note: Pastikan turtle dimulai dan diakhirkan dengan penup
    """
    
    turtle.penup()
    turtle.goto(point1)
    turtle.pendown()
    turtle.goto(point2)
    turtle.penup()

def process_movement(direction: str, distance: float) -> None:
    """
    Menggerakkan turtle berdasarkan perintah movement (up, down, left, right)
    """
    
    if direction == "up":
        t.setheading(90)
    elif direction == "down":
        t.setheading(270)
    elif direction == "left":
        t.setheading(180)
    elif direction == "right":
        t.setheading(0)

    # Pecah menjadi per langkah (biar bisa dicek setiap pergerakan & nggak nge-phase lewat dinding)
    steps = 5
    num_of_steps = int(distance // 5)
    rest_of_distance = distance % 5
    for i in range(num_of_steps, -1, -1):
        if i != 0:
            t.forward(steps)
        else:
            t.forward(rest_of_distance)
        if check_all_collisions():
            return 'COLLIDED'

    if is_at_finish():
        return 'FINISH'
    return ''

def move(direction: str, distance: float) -> None:
    """
    Memproses dan mendeteksi setiap gerakan turtle
    """
    # Keyword global agar variabel berikut bisa diakses dari scope local
    global collided, moving, trail, cockpit_coor

    # Move dibatalkan jika masih ada movement lain
    if moving:
        return

    moving = True

    # # Simpan posisi sebelum gerakan
    old_position = t.position()

    # Proses gerakan (turtle digerakkan)
    movement_status = process_movement(direction, distance)
    
    new_position = t.position()
    draw_line(old_position, new_position, tracker)
    
    t.update()

    moving = False

    return movement_status



# Segmen collision
def distance_to_line_segment(
    point: tuple[float, float],
    line_start: tuple[float, float],
    line_end: tuple[float, float],
) -> float:
    """
    Mengembalikan jarak terdekat suatu titik (point) ke segment garis tertentu
    """
    px = point[0]
    py = point[1]
    x1 = line_start[0]
    y1 = line_start[1]
    x2 = line_end[0]
    y2 = line_end[1]

    if x1 == x2 and y1 == y2:
        return math.hypot(px - x1, py - y1)

    dx = x2 - x1
    dy = y2 - y1
    length_squared = dx * dx + dy * dy
    t = max(0, min(1, ((px - x1) * dx + (py - y1) * dy) / length_squared))

    proj_x = x1 + t * dx
    proj_y = y1 + t * dy

    return math.hypot(px - proj_x, py - proj_y)

def is_collided(
    turtle_point: tuple[float, float],
    line_start: tuple[float, float],
    line_end: tuple[float, float],
) -> bool:
    """
    Mengecek apakah turtle menabrak dinding
    (tabrakan terjadi jika jarak turtle dengan dinding kurang dari 5)
    """
    jarak_ke_dinding = distance_to_line_segment(turtle_point, line_start, line_end)
    if jarak_ke_dinding < 5:
        return True

def is_at_finish() -> bool:
    """
    Mengecek apakah turtle mencapai finish
    (jika jarak turtle dengan finish kurang dari 25)
    """
    global escape_pod_coor

    turtle_point = t.position()
    px = turtle_point[0]
    py = turtle_point[1]
    escape_x = escape_pod_coor[0]
    escape_y = escape_pod_coor[1]

    jarak_ke_finish = math.hypot(px - escape_x, py - escape_y)
    if jarak_ke_finish < 25:
        return True


# Segmen Setup Window
def draw_grid(size: int, spacing: int) -> None:
    """
    Menggambarkan grid persegi dari (-size, -size) hingga (size, size)
    secara instan dengan warna #d3d3d3
    """
    t.tracer(0)
    old_color = t.color()
    t.color("#d3d3d3")
    t.penup()

    # Draw vertical lines
    # menghadap keatas dulu
    t.left(90)
    for x in range(-size, size, spacing):
        t.goto(x, -size)
        t.pendown()
        t.forward(2 * size)
        t.penup()

    # Draw horizontal lines
    # hadap kanan lagi
    t.right(90)
    for y in range(-size, size, spacing):
        t.goto(-size, y)
        t.pendown()
        t.forward(2 * size)
        t.penup()
        
    t.color(old_color[0])
    t.update()
    t.tracer(1)

def parse_point_string(point_Str: str) -> list[tuple[float, float]]:
    """
    Mengubah string koordinat menjadi list dari tuple points
    Ex. "12.34,56.78 87.65,43.21" -> [(12.34, 56.78), (87.65, 43.21)]
    """

    points_list_raw = point_Str.split()
    points_list = []
    for point_raw in points_list_raw:
        points_list.append(tuple(float(point) for point in point_raw.split(',')))
    return points_list


def draw_maze() -> list[tuple[tuple[float, float], tuple[float, float]]]:
    """
    Menggambar skema pesawat dari ship_map.cosmic secara instan
    Mengembalikan garis-garis pada skema pesawat
    """
    line_list = []
    xml_tree = ET.parse("ship_map.cosmic")  # Load .cosmic sebagai pohon xml
    namespaces = {"ns": "http://cosmic.cs"}  # Set namespace cosmic
    # Format namespace {<namespace>}<tag> (abaikan < dan >)
    # maka +2 kurung luar
    namespace_length = len(namespaces["ns"]) + 2
    # Gunakan library untuk list semua elemen dibawah namespace cosmic
    for element in xml_tree.iterfind(".//ns:*", namespaces):
        # Ambil tagnya saja (skip namespace dan kurung kurawal)
        match element.tag[namespace_length:]:
            case "polyline":
                # Polyline adalah beberapa garis dihubungkan satu sama lain
                points = parse_point_string(element.attrib["points"])
                for i in range(len(points) - 1):
                    line_list.append([points[i], points[i + 1]])
            case "line":
                # Line adalah 1 garis
                x1 = float(element.attrib["x1"])
                x2 = float(element.attrib["x2"])
                y1 = float(element.attrib["y1"])
                y2 = float(element.attrib["y2"])
                line_list.append([(x1, y1), (x2, y2)])
            case "polygon":
                # Polygon adalah polyline dimana titik akhir dan awal terhubung
                points = parse_point_string(element.attrib["points"])
                for i in range(len(points) - 1):
                    line_list.append([points[i], points[i + 1]])
                line_list.append([points[-1], points[0]])
            case "rect":
                # Rectangle = persegi panjang
                x = float(element.attrib["x"])
                y = float(element.attrib["y"])
                width = float(element.attrib["width"])
                height = float(element.attrib["height"])
                line_list.append([(x, y), (x + width, y)])
                line_list.append([(x + width, y), (x + width, y + height)])
                line_list.append([(x, y + height), (x + width, y + height)])
                line_list.append([(x, y), (x, y + height)])
    scale = 0.6
    x_offset = -440
    y_offset = 300
    # Fungsi tracer mengnonaktifkan update otomatis layar secara sementara
    t.tracer(0)
    for line in line_list:
        # Gambar setiap garis berdasarkan offset dan scale
        line[0] = (line[0][0] * scale + x_offset, -line[0][1] * scale + y_offset)
        line[1] = (line[1][0] * scale + x_offset, -line[1][1] * scale + y_offset)
        draw_line(line[0], line[1], t)
    t.update()  # Update layar secara manual
    t.tracer(1)  # Aktifkan lagi update otomatis layar
    return line_list

def death_message():
    """Returns a Death Message."""
    death_message = 'Path tidak mencapai destinasi; gagal keluar dari kapal.\nTerjadi tabrakan dengan asteroid, mengguncang kapal. Pintu keluar dari kokpit tertutup oleh reruntuhan.\nKini program simulasi ini tak dapat menyelamatkan anda lagi.\nSebuah planet merah terlihat jelas di jendela kokpit, seolah-olah membesar seiring mendekatnya kapal dengan kecepatan yang dahsyat.\nAnda dengan harapan-harapan terakhir anda mencoba mengembalikan kontrol, namun sekarang sudah terlambat.\n\033[31mKau mengecewakanku, Dek Depe.\033[0m'
            
    return death_message

def init_screen() -> t._Screen:
    """
    Initialisasi turtle Screen dengan
    - Setup window seukuran 1500x1000
    - Title "COSMIC Escape Simulator"
    Lalu kembalikan objek Screen tersebut
    """
    screen = t.Screen()
    screen.title("COSMIC Escape Simulator")
    screen.setup(width=1500, height=1000)
    
    return screen

def init_tracker():
    tracker = t.Turtle()
    tracker.color("blue")
    tracker.hideturtle()
    return tracker

def update_tracker(fail_counter: int = 0):
    # Tulis counter fail (di pojok)
    tracker.penup()
    tracker.goto(360, -300)
    tracker.pendown()
    tracker.write(fail_counter, font=("Arial", 20, "normal"))


# Eksekusi
if __name__ == "__main__":
    # Inisialisasi layar
    screen = init_screen()

    # Gambar grid dan pesawat
    draw_grid(1000, 10)
    line_list = draw_maze()
    
    # Inisasi turtle
    t.goto(cockpit_coor)
    t.showturtle()
    t.penup()
    # hadap kiri biar kesannya lagi mau kabur
    t.setheading(180)

    # Inisialisasi tracker (turtle biru)
    tracker = init_tracker()

    # Mendefinisikan pengecekan tabrakan terharap semua garis
    def check_all_collisions():
        global collided
        for line in line_list:
            if is_collided(t.pos(), line[0], line[1]) and not collided:
                return True


    # Set fokus pada turtle screen
    screen.listen()

    # Penggambaran dipercepat
    t.speed(0)
    t.delay(0)


    fail_counter = 0
    while True:
        direction = input('Masukkan arah (up, down, left, right, end): ')
        if direction == 'end':
            print(death_message())
            # Exit dengan tidak hormat
            exit()
        distance = float(input('Masukkan jarak: '))
        
        movement_status = move(direction, distance)

        # Handle kedua case: collided dan finish
        if movement_status == 'COLLIDED':
            if fail_counter == 0:
                print("Anda menabrak dinding! Setiap kesalahan akan menambah fail counter anda.")
            else:
                print("Dinding tertabrak! Kembali ke titik awal...")
            fail_counter += 1
            # Reset posisi turtle dan garis2 tracker
            t.goto(cockpit_coor)
            
            tracker.clear()
            update_tracker(fail_counter)

        if movement_status == 'FINISH':
            print('Berhasil kabur!')
            # Display stats terakhir
            if fail_counter == 0:
                attempts = 'sekali percobaan! LUAR BIASA ✨✨✨'
            else:
                attempts = f'{fail_counter} kali percobaan!'
            print(f'Anda kabur dalam {attempts}')
            # Exit dengan terhormat
            exit()
        

# sejujurnya, reaksi saya ttg lab ini yaitu SAYA GA NGERTI
# saya kebingungan nyari alur... misalnya, ada function yang selalu cek collision, tapi di segmen move disuruh lakukan cek lagi.
# (yang disuruh digunakan yaitu is_collided())
# nah, terus saya ketemu kalo ternyata ada turtle lagi yg namanya tracker. saya dari awal gak nyadar ada itu
# intinya saya kesulitan berat hehe