from flask import Flask, jsonify
from flask_cors import CORS  # Импортируем CORS
import sqlite3
import os
import base64

app = Flask(__name__)
CORS(app)  # Включаем CORS для всего приложения

# Маршрут для получения всех отзывов
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()

    # Извлекаем все отзывы из базы
    cursor.execute("SELECT id, name, photo, text FROM reviews")
    rows = cursor.fetchall()
    conn.close()

    # Преобразуем данные в JSON-формат
    reviews = []
    for row in rows:
        review = {
            "id": row[0],
            "name": row[1],
            "photo": base64.b64encode(row[2]).decode('utf-8') if row[2] else None,  # Преобразуем фото в Base64
            "text": row[3]
        }
        reviews.append(review)

    return jsonify(reviews)

@app.route('/')
def home():
    return "API is running. Access the reviews endpoint at /api/reviews"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Получаем порт из переменных окружения
    app.run(host="0.0.0.0", port=port, debug=True)
