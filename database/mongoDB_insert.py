from pymongo import MongoClient


def insert_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.local  # 'local' 데이터베이스 사용

    # 책 데이터 삽입
    books = [
        {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987},
        {"title": "1Q84", "author": "Haruki Murakami", "year": 2009},
    ]
    db.books.insert_many(books)

    # 영화 데이터 삽입
    movies = [
        {
            "title": "Inception",
            "director": "Christopher Nolan",
            "year": 2010,
            "rating": 8.8,
        },
        {
            "title": "Interstellar",
            "director": "Christopher Nolan",
            "year": 2014,
            "rating": 8.6,
        },
        {
            "title": "The Dark Knight",
            "director": "Christopher Nolan",
            "year": 2008,
            "rating": 9.0,
        },
    ]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = [
        {"user_id": 1, "action": "click", "timestamp": "2023-04-12T08:00:00Z"},
        {"user_id": 1, "action": "view", "timestamp": "2023-04-12T09:00:00Z"},
        {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T10:00:00Z"},
    ]
    db.user_actions.insert_many(user_actions)

    print("Data inserted successfully")
    client.close()


if __name__ == "__main__":
    insert_data()
