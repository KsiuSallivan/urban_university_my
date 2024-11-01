import math


class Figure:

    sides_count = 0

    def __init__(self, color, *sides):

        if len(sides) != self.sides_count:
            self.__sides = sides[0]*self.sides_count
        else:
            self.__sides = [i for i in sides]

        self.__color = list(color) # список цветов в формате RGB
        self.filled = False # закрашенный, bool

    def get_color(self):
        """ возвращает список RGB цветов"""
        return self.__color

    def __is_valid_color(self, r, g, b):
        """ принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета.
        Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно)"""

        for i in (r, g, b):
            if not (isinstance(i, int) and 0 <= i <= 255):
                return False

        return True

    def set_color(self, r, g, b):
        """ принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
        предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним."""
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

        return self.__color

    def __is_valid_sides(self, *args):
        """ принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа
        и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях."""

        for i in args:
            if not (isinstance(i, int) and i > 0):
                return False

        if len(args) != self.sides_count:
            return False

        return True

    def get_sides(self):
        """ должен возвращать значение атрибута __sides"""
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        """ должен принимать новые стороны, если их количество не равно sides_count, то не изменять,
        в противном случае - менять"""

        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):

    def __init__(self, color, side):
        self.sides_count = 1
        super().__init__(color, side)
        self.__radius = side / (2 * math.pi)

    def get_square(self):
        """ возвращает площадь круга (можно рассчитать как через радиус)"""
        square = math.pi * (self.__radius ** 2)
        return square


class Triangle(Figure):

    sides_count = 3

    def get_square(self):
        """ возвращает площадь треугольника. (можно рассчитать по формуле Герона)"""
        sides = self.get_sides()
        p = sum(sides) / 2
        square = math.sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))
        return square


class Cube(Figure):

    def __init__(self, color, side):
        self.sides_count = 12
        super().__init__(color, [side])
        self.__sides = side * 12

    def get_volume(self):
        """ возвращает объём куба."""
        side = self.get_sides()[0]
        square = side ** 3
        return square



# test urban

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print('Цвет меняется - должно быть [55, 66, 77]')
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print('Цвет НЕ меняется - должно быть [222, 35, 130]')
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print('Стороны куба НЕ меняются - должно быть [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]')
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print('Окружность меняется - должно быть [15]')
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print('Периметр круга,  - как в предыдущем пункт должно быть 15')
print(len(circle1))

# Проверка объёма (куба):
print('Объем куба,  - должен быть 216')
print(cube1.get_volume())

