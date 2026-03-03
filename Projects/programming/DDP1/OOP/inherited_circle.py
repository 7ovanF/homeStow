from point import *
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
class CartesianCircle(Circle):
    def __init__(self, radius, x, y):
        super().__init__(radius)
        self.center_point = Point(x, y)
        