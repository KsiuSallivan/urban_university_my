def custom_write(file_name, strings):

    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')

    for line_num, string in enumerate(strings, start=1):
        byte_num = file.tell()
        file.write(string + '\n')
        strings_positions[(line_num, byte_num)] = string

    file.close()

    return strings_positions


# test
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
