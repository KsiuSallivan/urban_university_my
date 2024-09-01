def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params() # вывод: 1 строка True
print_params(b=25) # вывод: 1 25 True
print_params(c=[1,2,3]) # вывод: 1 строка [1, 2, 3]


values_list = ['difficult', 25, True]
values_dict = {'a': '1', 'b': 'строка', 'c': 'True'}

print_params(*values_list) # вывод: difficult 25 True
print_params(**values_dict) # вывод: 1 строка True


values_list_2 = ['stress', 100500]

print_params(*values_list_2, 42) # вывод: stress 100500 42
