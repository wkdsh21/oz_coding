from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.local
db.books.update_many({"genre": {"$exists": False}}, {"$set": {"genre": "fantasy"}})


# [문제 1: 특정 장르의 책 찾기]
def find_books_by_genre(db, genre):
    books = db.books.find({"genre": genre}, {"_id": 0, "title": 1, "author": 1})
    for book in books:
        print(book)


# [문제 2: 감독별 평균 영화 평점 계산]
def movies_avg_rating_by_director(db):
    movies = db.movies.aggregate(
        [
            {"$group": {"_id": "$director", "avg_rating": {"$avg": "$rating"}}},
            {"$sort": {"avg_rating": -1}},
        ]
    )
    for movie in movies:
        print(movie)


# [문제 3: 특정 사용자의 최근 행동 조회]
def find_actions_by_user(db, user_id):
    actions = (
        db.user_actions.find({"user_id": user_id}, {"_id": 0})
        .sort({"timestamp": -1})
        .limit(5)
    )
    for action in actions:
        print(action)


# [문제 4: 출판 연도별 책의 수 계산]
def sum_books_by_pubyear(db):
    book_counts = db.books.aggregate(
        [
            {"$group": {"_id": "$year", "sum_books": {"$sum": 1}}},
            {"$sort": {"sum_books": -1}},
        ]
    )
    for book_count in book_counts:
        print(book_count)


# [문제 5: 특정 사용자의 행동 유형 업데이트]
def update_actions_by_user(db, user_id, year):
    db.user_actions.update_many(
        {"user_id": user_id, "timestamp": {"$lt": year}, "action": "view"},
        {"$set": {"action": "seen"}},
    )


# update_actions_by_user(db, 1, "2023-04-13T09:00:00Z")
