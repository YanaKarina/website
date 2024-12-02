import sqlite3

# Подключаемся к SQLite (создаётся файл reviews.db, если его нет)
conn = sqlite3.connect('reviews.db')

# Создаём курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаём таблицу "reviews", если её нет
cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    photo BLOB,
    text TEXT NOT NULL
)
''')

# Примерные данные для добавления
reviews = [
    {
        "name": "Иван Иванов",
        "photo": "chel_otz.jpg",
        "text": "Отличный сайт, помог разобраться быстро!"
    },
    {
        "name": "Анна Смирнова",
        "photo": "chel_otz2.jpg",
        "text": "Очень удобный и современный интерфейс!"
    },
    {
        "name": "Алексей Петров",
        "photo": "chel_otz3.jpg",
        "text": "Классный проект, всё интуитивно понятно."
    },
    {
        "name": "Мария Васильева",
        "photo": "chel_otz4.jpg",
        "text": "Проект впечатлил, надеюсь на дальнейшее развитие."
    },
    {
        "name": "Дмитрий Ковалев",
        "photo": "chel_otz5.jpg",
        "text": "Рекомендую всем, кто хочет лёгкость в использовании."
    },
    {
        "name": "Екатерина Сидорова",
        "photo": "chel_otz6.jpg",
        "text": "Удобно, красиво и быстро работает!"
    }
]

# Добавление отзывов с фотографиями в таблицу
for review in reviews:
    with open(review["photo"], 'rb') as file:
        photo_data = file.read()  # Читаем фото как байты
        cursor.execute(
            "INSERT INTO reviews (name, photo, text) VALUES (?, ?, ?)",
            (review["name"], photo_data, review["text"])
        )

# Сохраняем изменения
conn.commit()
conn.close()
