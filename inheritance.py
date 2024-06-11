import math


class Figure:
    def __init__(self):
        pass

    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class RectangleTriangle(Figure):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height)/2


class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        super().__init__()
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return ((self.base1 + self.base2) * self.height)/2


class Figure:
    def __init__(self):
        pass

    def area(self):
        pass

    def __int__(self):
        return self.area()

    def __str__(self):
        return {self.__class__.__name__}


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __int__(self):
        return self.area()

    def __str__(self):
        return f"Прямоугольник: ширина = {self.width}, высота = {self.height}"


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __int__(self):
        return self.area()

    def __str__(self):
        return f"Окружность: радиус = {self.radius}"


class RectangleTriangle(Figure):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height)/2

    def __int__(self):
        return self.area()

    def __str__(self):
        return f"Прямоугольный треугольник: основание = {self.base}, высота = {self.height}"


class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        super().__init__()
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return ((self.base1 + self.base2) * self.height)/2

    def __int__(self):
        return self.area()

    def __str__(self):
        return f"Трапеция: основание1 = {self.base1}, основание2 = {self.base2}, высота = {self.height}"


rectangle = Rectangle(5, 8.5)
print(rectangle.area())
print(str(rectangle))

circle = Circle(4.1)
print(circle.area())
print(str(circle))

rectangle_triangle = RectangleTriangle(5, 7.3)
print(rectangle_triangle.area())
print(str(rectangle_triangle))

trapezoid = Trapezoid(5.5, 3, 2.4)
print(trapezoid.area())
print(str(trapezoid))
