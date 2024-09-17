data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):

    # Делаем из списка чистую строку
    def make_string(data_structure):
        h = str(data_structure)
        s1 = h.replace('[', '')
        s2 = s1.replace(']', '')
        s3 = s2.replace('(', '')
        s4 = s3.replace(')', '')
        s5 = s4.replace('{', '')
        s6 = s5.replace('}', '')
        s7 = s6.replace(':', '')
        s8 = s7.replace(',', '')
        s9 = s8.replace("'", '')
        s10 = s9.replace('  ', ' ')
        data_string = s10.split()
        return data_string


    # Делаем из общей строки 2 списка - с цифрами(пока как строки) и с длинами строк
    number_list = []
    string_list = []
    for i in make_string(data_structure):
        if i.isdigit():
            number_list.append(i)
        elif i in str([0,1,2,3,4,5,6,7,8,9]):
            number_list.append(i)
        else:
            string_list.append(len(i))


    # Делаем сумму цифр
    number_sum = 0
    for i in number_list:
        number_sum = number_sum + int(i)


    # Делаем сумму длин строк
    string_sum = 0
    for i in string_list:
        string_sum = string_sum + i


    # Возвращаем результат сложения
    return number_sum + string_sum


result = calculate_structure_sum(data_structure)
print(result)

# ---подсказка с вебинара
# def calculate_structure_sum(data_structure):
# # result = 0
# # if если данные int
# # elif если данные str
# elif isinstance(data_structure, (list, tuple, set)):
#     for el in data_structure:
#         result +=calculate_structure_sum(el)
# elif isinstance(data_structure, dict):
#
# return result
