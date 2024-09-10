class Vehicle:
    __COLOR_VARIANTS = ['red', 'pink', 'black', 'yellow']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__color = str(__color)
        self.__engine_power = int(__engine_power)

    def get_model(self, __model):
        return f'Модель: {__model}'

    def get_horsepower(self, __engine_power):
        return f'Мощность двигателя: {__engine_power}'

    def get_color(self,__color):
        return f'Цвет: {__color}'

    def print_info(self):
        print(self.get_model(self))
        print(self.get_horsepower(self))
        print(self.get_color(self))
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color, ):

        for i in range(len(self.__COLOR_VARIANTS)):
            self.__COLOR_VARIANTS[i] = self.__COLOR_VARIANTS[i].lower()

        if str(new_color).lower() in self.__COLOR_VARIANTS:
            return self.__color == new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5




# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()
#
# # Меняем свойства (в т.ч. вызывая методы)
# vehicle1.set_color('Pink')
# vehicle1.set_color('BLACK')
# vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
# vehicle1.print_info()