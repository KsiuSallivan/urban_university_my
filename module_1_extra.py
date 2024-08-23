grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # списки оценок для каждого ученика в алфавитном порядке
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # неупорядоченная последовательность имён всех учеников в классе

students_alphabet = sorted(list(students)) # превращаем множество в список, сортируем его, передаем в переменную

# Идей, как перебрать список без цикла с помощью только изученного, у меня не нашлось.
average_grade_list = [] # задаем пустой список, в котором будут отражены средние оценки
for grade in grades:
    average_grade = sum(grade) / len(grade)
    average_grade_list.append(average_grade) # с помощью цикла заполняем список средних оценок

# Думать и гуглить по заданию не запрещалось.
class_journal = dict(zip(students_alphabet, average_grade_list)) # объединяем 2 списка в словарь с помощью служебной команды
print(class_journal)




