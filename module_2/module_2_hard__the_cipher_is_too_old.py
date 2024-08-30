from itertools import combinations, chain
from operator import sub


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


divisors_of_my_random_number = find_divisors(random_number)
# print('Делители для числа: ')
# print(divisors_of_my_random_number)


# Находим сумму чисел для каждого делителя
# TODO (эта функция найдена в интернете, сама не нашла решение из известных мне знаний, буду рада подсказке)
def sum_to_n(i):
    b, mid, e = [0], list(range(1, i)), [i]
    splits = (d for i in range(i) for d in combinations(mid, i))
    return (list(map(sub, chain(s, e), chain(b, s))) for s in splits)


# Находим пары
list_summers = []
for i in divisors_of_my_random_number:
    for p in sum_to_n(i):
        if len(p) == 2:
            list_summers.append(sorted(p))
# print(list_summers)


# Фильтруем уникальные пары
tuple_of_pairs = set(sorted(tuple(i) for i in list_summers))

list_of_pairs = []
for k,l in tuple_of_pairs:
    list_of_pairs.append(str(k)+str(l))
# print(sorted(list_of_pairs))


# Выводим все полученные уникальные пары в сортированную строку
string_of_pairs = ("".join(sorted(list_of_pairs)))
print(string_of_pairs)

