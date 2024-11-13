import sqlite3

# Создание базы данных и подключение к ней
conn = sqlite3.connect('not_telegram_2.db')
cursor = conn.cursor()

# Создание таблицы Users, если она еще не создана
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                  (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, age INTEGER, balance INTEGER NOT NULL)''')
# Заполнение таблицы 10 записями
users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]
cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users)

# Обновление баланса у каждой 2-й записи, начиная с 1-й
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")
# Удаление каждой 3-й записи, начиная с 1-й
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
# Выборка всех записей, где возраст не равен 60, и вывод в консоль
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
for row in cursor.fetchall():
    username, email, age, balance = row
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчет общего количества записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(f"Общее количество записей: {total_users}")

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(f"Сумма всех балансов: {all_balances}")

# Вывод среднего баланса
average_balance = all_balances / total_users
print(f"Средний баланс: {average_balance}")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()