immutable_var = ('Ksiu', 39, True, ['books', 'plants'])
print('Immutable tuple: '+ str(immutable_var))

# immutable_var[0] = 8
# print(immutable_var)
# Итог: TypeError: 'tuple' object does not support item assignment - кортеж относится к неизменяемому типу


mutable_list = ['Ksiu', 39, True,]
mutable_list[1] = 100500
print('Mutable list: ' + str(mutable_list))
