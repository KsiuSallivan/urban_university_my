import math


class Figure:
    def __init__(self, color, sides):
        self.sides_count = 0
        self.__sides = list(sides) # список сторон (целые числа)
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
            if not (isinstance(i, int) and 0 < i):
                return False

        if len(args) != self.sides_count:
            return False

        return True

    def get_sides(self):
        """ должен возвращать значение атрибута __sides"""
        return self.__sides

    def __len__(self):
        """ должен возвращать периметр фигуры"""
        len_sides = 0
        for i in self.__sides:
            len_sides += i
        return len_sides

    def set_sides(self, *new_sides):
        """ должен принимать новые стороны, если их количество не равно sides_count, то не изменять,
        в противном случае - менять"""
        sides_list = []
        if len(new_sides) == self.sides_count:
            if self.__is_valid_sides(*new_sides):
                self.__sides = new_sides
        # else:
        #     for i in range(self.sides_count+1):
        #         sides_list.append(1)
        #     self.__sides = sides_list

        return self.__sides


class Circle(Figure):
    def __init__(self, color, side):
        self.sides_count = 1
        super().__init__(color, [side])
        self.__radius = side / (2*math.pi)


    def get_square(self):
        """ возвращает площадь круга (можно рассчитать как через длину, так и через радиус)"""
        square = math.pi * (self.__radius ** 2)
        return square


class Triangle(Figure):
    def __init__(self, color, sides):
        self.sides_count = 3
        super().__init__(color, sides)

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
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

