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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(4, 9))
