import turtle
import math

def cos(angle):
    cos = math.cos(math.radians(angle))
    return cos
def sin(angle):
    sin = math.sin(math.radians(angle))
    return sin
def asin(sin_angle):
    angle = math.degrees((math.asin(sin_angle)))
    return angle

movt_a = 150
turn_a = 45
movt_b = 90
# kalkulasi movt_c agar sampai ke titik awal
# rumus : c^2 = a^2 + b^2 - 2ab * cos(C)
angl_C = 180 - turn_a
movt_c = math.sqrt((movt_a * movt_a) + (movt_b * movt_b) - 2 * movt_a * movt_b * cos(angl_C))
# rumus : sin(A) = a / (c / sin(C))
sin_angl_A = movt_a / (movt_c / sin(angl_C))
angl_A = asin(sin_angl_A)
turn_b = 180 - angl_A

turtle.forward(movt_a)
turtle.right(turn_a)
turtle.forward(movt_b)
turtle.right(turn_b)
turtle.forward(movt_c)

turtle.mainloop()
