first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = [len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b)]

second_result = [len(first[i]) == len(second[i]) for i in range(min(len(first), len(second)))]
# В задаче указаны списки одинаковой длины, но ведь могут быть и разные, поэтому использовала min


# test
print(list(first_result))
print(list(second_result))