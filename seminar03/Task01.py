#  Контекст
# Предположим, что мы хотим написать программу для исследования геометрических фигур. Для того 
# чтобы это сделать мы решили начать с создания абстрактного класса - “Фигура”.
# ● Задача
# Реализовать класс Shape, содержащий пустые методы get_area и get_perimeter. Использовать библиотеку 
# абстрактных классов “ABC” в данном случае - не обязательно.


# class Shape:
#     def get_area(self):
#         pass

#     def get_perimeter(self):
#         pass


# from abc import ABCMeta, abstractmethod


# class Shape:
#     __metaclass__ = ABCMeta

#     @abstractmethod
#     def get_area(self):
#         pass

#     @abstractmethod
#     def get_perimeter(self):
#         pass


#     ● Контекст
# Теперь, когда у вас есть абстрактный класс Shape, ваша следующая задача - получить класс Circle.
# ● Задача
# Реализовать дочерний от Shape класс Circle, включая следующие работающие методы:
# ○ конструктор класса __init__ - метод инициализации класса Circle.
# ○ get_area - метод для расчета площади круга
# ○ get_perimeter - метод для расчета периметра окружности

# class Circle(Shape):
#     def __init__(self, diameter):
#         super().__init__(diameter=diameter)

#     @property
#     def diameter(self):
#         return self._diameter

#     @diameter.setter
#     def diameter(self, value):
#         self._diameter = value

#     def perimeter(self):
#         return pi * self.diameter

#     def area(self):
#         return pi * (self.diameter/2)**2


import math


class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self._radius = r
        self.pi = math.pi

    def get_area(self):
        return self.pi * self._radius ** 2

    def get_perimeter(self):
        return 2 * (self.pi * self._radius)

    def get_radius(self):
        return self._radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

a = Circle(10)
a._radius = "sss"




import math
from abc import ABCMeta, abstractmethod


class Shape:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius: int):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
# треугольник

class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


# Task 3
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        return (self.a * self.b) / 2

    def get_perimeter(self):
        return self.a + self.b + self.c
    

class RightTriangle(Triangle):
    def __init__(self, leg1, leg2):
        hypotenuse = (leg1 ** 2 + leg2 ** 2) ** 0.5
        super().__init__(leg1, leg2, hypotenuse)

    @property
    def leg1(self):
        return self.side1

    @leg1.setter
    def leg1(self, value):
        hypotenuse = (value ** 2 + self.leg2 ** 2) ** 0.5
        super().__init__(value, self.leg2, hypotenuse)

    @property
    def leg2(self):
        return self.side2

    @leg2.setter
    def leg2(self, value):
        hypotenuse = (self.leg1 ** 2 + value ** 2) ** 0.5
        super().__init__(self.leg1, value, hypotenuse)

    @property
    def hypotenuse(self):
        return self.side3

    @hypotenuse.setter
    def hypotenuse(self, value):
        if value < (self.leg1 ** 2 + self.leg2 ** 2) ** 0.5:
            raise ValueError("Hypotenuse is too short")
        super().__init__(self.leg1, self.leg2, value)

    def perimeter(self):
        return self.leg1 + self.leg2 + self.hypotenuse

    def area(self):
        return 0.5 * self.leg1 * self.leg2



class Triangle(Shape):

def __init__(self, a: int, b: int):
self.b = b
self.a = a

def get_area(self):
return self.a * self.b / 2

def get_perimeter(self):
return (self.a + self.b) + (self.a ** 2 + self.b ** 2) ** 0.5



class Triangle(Shape):
def __init__(self, a, b, c):
self.a = a
self.b = b
self.c = c

def get_perimeter(self):
return self.a + self.b + self.c

def get_area(self):
p = self.get_perimeter() / 2
return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** .5


tr = Triangle(2, 2, 2)
print(f'{tr.get_perimeter()=}, {tr.get_area()=}')