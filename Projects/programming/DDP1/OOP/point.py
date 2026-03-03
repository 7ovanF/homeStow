import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def __str__(self):
        return f"Point: x = {self.__x}, y = {self.__y}"
        
    def get_x(self):
        return self.__x
        
    def get_y(self):
        return self.__y
        
    def get_point(self):
        return (self.__x, self.__y)
        
    def move(self, new_x, new_y):
        self.__x = new_x
        self.__y = new_y
        
    def distance(self, other_point):
        x_distance = other_point.get_x() - self.get_x()
        y_distance = other_point.get_y() - self.get_y()
        return math.sqrt(x_distance ** 2 + y_distance ** 2)

class LabelledPoint(Point):
    def __init__(self, x, y, label):
        super().__init__(x, y)
        self.__label = label
    def get_label(self):
        return self.__label