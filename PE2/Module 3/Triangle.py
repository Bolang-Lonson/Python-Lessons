import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        dx = self.__x - x
        dy = self.__y - y
        dist = math.hypot(dx, dy)
        return dist

    def distance_from_point(self, point):
        dx = self.__x - point.getx()
        dy = self.__y - point.gety()
        dist = math.hypot(dx, dy)
        return dist


class Triangle:
    def __init__(self, vertex1, vertex2, vertex3):
        self.__vertices = [vertex1, vertex2, vertex3]

    def perimeter(self):
        d12 = self.__vertices[0].distance_from_point(self.__vertices[1])
        d23 = self.__vertices[1].distance_from_point(self.__vertices[2])
        d13 = self.__vertices[0].distance_from_point(self.__vertices[2])
        return d12 + d23 + d13


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
