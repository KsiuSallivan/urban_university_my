import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 1
        while self.enemies > 0:
            self.enemies -= self.power
            print(f"{self.name}, сражается {days} день(дня)..., осталось {self.enemies} воинов.")
            time.sleep(1)
            days += 1
        print(f"{self.name} одержал победу спустя {days-1} дней(дня)!")


# test
# Создание объектов класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Создание и запуск потоков
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")