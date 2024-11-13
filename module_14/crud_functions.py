import sqlite3


def initiate_db():
    conn = sqlite3.connect('not_telegram_4.db')
    cursor = conn.cursor()

    # Создание таблицы Products, если она еще не создана
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products
                      (id INTEGER PRIMARY KEY, title TEXT NOT NULL, description TEXT, price INTEGER NOT NULL)''')

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('not_telegram_4.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    conn.close()
    return products
