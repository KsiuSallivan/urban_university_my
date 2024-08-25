# от старой ненужной домашки про список оставлю себе историю:
# my_list = ['lamp', 'book', 'table', 'pen', 'paper']
# print(my_list)
# print(my_list[0])
# print(my_list[-1])
# print(my_list[2:5])
# my_list[2] = 'camera'
# print(my_list)

# словари
my_dict = {'lamp': 'лампа', 'book': 'книга', 'table': 'стол', 'pen': 'ручка', 'paper': 'бумага'}
print(my_dict)
print(my_dict.get('book'))
print(my_dict.get('camera'))
my_dict.update({'laptop': 'ноутбук', 'camera': 'камера'})
deleted_item = my_dict.pop('lamp')
print(deleted_item)
print(my_dict)

# множества
my_set = {1, 2, 'lamp', 'book', 2, 5, 'book', True}
print(my_set)
my_set.update(['face', 6])
my_set.discard(2)
print(my_set)
