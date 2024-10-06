import pymysql


def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            connection.commit()


# 데이터베이스 연결 설정
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="4463",
    db="airbnb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

try:
    # 1.새로운 제품 추가
    execute_query(
        connection,
        "INSERT INTO Products(productName,price,stockQuantity) VALUES(%s,%s,%s)",
        ("oz_book", 3000, 100),
    )

    # 2.고객 목록 조회
    print(execute_query(connection, "SELECT * FROM Customers"))

    # 3.제품 재고 업데이트
    execute_query(
        connection,
        "UPDATE Products SET stockQuantity=stockQuantity-%s WHERE productID=%s",
        (10, 4),  # (amount, productId)
    )

    # 4.고객별 총 주문 금액 계산
    print(
        execute_query(
            connection,
            "SELECT customerID,sum(totalAmount) FROM Orders GROUP BY customerID",
        )
    )

    # 5.고객 이메일 업데이트
    execute_query(
        connection,
        "UPDATE customers SET email=%s WHERE customerId=%s",
        ("michardorr@example.net", 1),
    )

    # 6.주문 취소
    execute_query(connection, "DELETE FROM Orders WHERE orderId=%s", (1))

    # 7.특정 제품 검색
    print(
        execute_query(
            connection, "SELECT * FROM Products WHERE productName = %s", ("Read Car")
        )
    )

    # 8.특정 고객의 모든 주문 조회
    print(execute_query(connection, "SELECT * FROM Orders WHERE customerId = %s", (1)))

    # 9.가장 많이 주문한 고객 찾기
    print(
        execute_query(
            connection,
            "SELECT * FROM Customers WHERE customerId = (SELECT customerId FROM Orders GROUP BY customerId ORDER BY sum(totalAmount) DESC LIMIT 1)",
        )
    )

finally:
    # 데이터베이스 연결 종료
    connection.close()
