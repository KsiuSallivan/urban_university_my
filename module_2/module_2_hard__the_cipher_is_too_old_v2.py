# Вводим число, от которого все зависит
random_number = int(input("Введите число от 3 до 20: "))
if (int(random_number)) < 3 or (int(random_number)) > 20:
    print('Неверный ввод, вы обречены')
else:
    print(random_number)


# Находим делители указанного числа
def find_divisors(random_number):
    divisors = []
    for i in range(1, random_number+1):
        if random_number % i == 0:
            divisors.append(i)
    return divisors


# Находим парные слагаемые для каждого делителя
list_summers = []
for i in find_divisors(random_number):
    for j in range(1, i):
        for k in range(1, i):
            if j + k == i:
                list_summers.append(str(j)+str(k))


# Набираем уникальные пары
filter_pairs_step_1 = []
for i in list_summers:
    filter_pairs_step_1.append(tuple(sorted(i)))

filter_pairs_step_2 = set(filter_pairs_step_1)


# Полученные данные вытаскиваем из кортежей в список отдельных цифр
list_of_pairs = []
for i in filter_pairs_step_2:
    list_of_pairs.extend(list(i))


# Выводим полученные цифры в строку
string_of_pairs = ''.join(list_of_pairs)
print(string_of_pairs)

