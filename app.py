import os
from flask import Flask, request
import pymysql

# Flask 애플리케이션 초기화
app = Flask(__name__)

# 환경 변수에서 DB 연결 정보 가져오기
db_host = os.getenv('MYSQL_HOST')
db_port = int(os.getenv('MYSQL_PORT', 3306))
db_user = os.getenv('MYSQL_USER')
db_password = os.getenv('MYSQL_PASSWORD')
db_name = os.getenv('MYSQL_DATABASE')

# MySQL 연결 함수
def connect_to_db():
    return pymysql.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor,  # 딕셔너리 형태로 결과 반환
    )

# 입력 페이지 렌더링
@app.route('/')
def index():
    return """
    <h1>상품 관리</h1>
    <form method="POST" action="/add">
        <label for="item">물건 이름:</label><br>
        <input type="text" id="item" name="item"><br>
        <label for="price">가격:</label><br>
        <input type="number" id="price" name="price"><br><br>
        <button type="submit">추가</button>
    </form>
    <br>
    <a href="/items">저장된 상품 보기</a>
    """

# 데이터 추가 처리
@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form.get('item')
    price = request.form.get('price')

    try:
        connection = connect_to_db()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO items (name, price) VALUES (%s, %s)", (item_name, price))
        connection.commit()
    except Exception as e:
        return f"<h1>오류 발생: {e}</h1><br><a href='/'>다시 시도하기</a>"
    finally:
        connection.close()

    return f"<h1>상품 '{item_name}'가 {price}원으로 저장되었습니다!</h1><br><a href='/'>다시 입력하기</a>"

# 저장된 데이터 보기
@app.route('/items')
def view_items():
    try:
        connection = connect_to_db()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM items")
            items = cursor.fetchall()
    except Exception as e:
        return f"<h1>오류 발생: {e}</h1><br><a href='/'>다시 시도하기</a>"
    finally:
        connection.close()

    # 조회된 데이터를 HTML로 표시
    html = "<h1>저장된 상품 목록</h1><ul>"
    for item in items:
        html += f"<li>{item['name']} - {item['price']}원</li>"
    html += "</ul><br><a href='/'>상품 추가하기</a>"

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
