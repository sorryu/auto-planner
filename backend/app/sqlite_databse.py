import sqlite3
from flask import Flask, request, jsonify
app = Flask(__name__)

# 사용자 테이블 생성
def create_user_tables():
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        nickname TEXT NOT NULL,
        password TEXT NOT NULL,
        mbti TEXT NOT NULL
    )
    ''')

# 카테고리 테이블 생성 
def create_category_tables():
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS category (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL,
        duration INTEGER,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    ''')

    # 강의 테이블 생성
def create_lecture_tables():
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS lecture (
        lecture_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER,
        lecture_name TEXT NOT NULL,
        duration INTEGER,
        FOREIGN KEY (category_id) REFERENCES category(category_id)
    )
    ''')

# 할 일 목록 테이블 생성
def create_to_do_list_tables():
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS to_do_list (
        to_do_list_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        achievement_or_not INTEGER NOT NULL,
        lecture_id INTEGER,
        FOREIGN KEY (lecture_id) REFERENCES lecture(lecture_id)
    )
    ''')

    conn.commit()
    conn.close()

# # 테이블 생성 함수 실행
# create_user_tables()

# 사용자 등록 함수
def register_user(name, nickname, password, mbti):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO users (name, nickname, password, mbti) 
        VALUES (?, ?, ?, ?)
        ''', (name, nickname, password, mbti))
        conn.commit()
        print("User registered successfully")
    except sqlite3.IntegrityError:
        print("User nickname already exists")
    finally:
        conn.close()
        
# 로그인 함수
def login_user(nickname, password):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT user_id FROM users WHERE nickname = ? AND password = ?
    ''', (nickname, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login successful")
        return user[0]
    else:
        print("Invalid credentials")
        return None

# 카테고리 추가 함수
def add_category(category_name, duration, user_id):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO category (category_name, duration, user_id) 
    VALUES (?, ?, ?)
    ''', (category_name, duration, user_id))
    conn.commit()
    conn.close()

    print("Category added successfully")

# 강의 추가 함수
def add_lecture(category_id, lecture_name, duration):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO lecture (category_id, lecture_name, duration) 
    VALUES (?, ?, ?)
    ''', (category_id, lecture_name, duration))
    conn.commit()
    conn.close()

    print("Lecture added successfully")

# 할 일 추가 함수
def add_to_do(date, achievement_or_not, lecture_id):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO to_do_list (date, achievement_or_not, lecture_id) 
    VALUES (?, ?, ?)
    ''', (date, achievement_or_not, lecture_id))
    conn.commit()
    conn.close()

    print("To-do item added successfully")




# 사용자 정보 조회 함수
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        user_data = {
            "user_id": user[0],
            "name": user[1],
            "nickname": user[2],
            "mbti": user[4]
        }
        return jsonify(user_data), 200
    else:
        return jsonify({"message": "User not found"}), 404


# 카테고리 조회 함수
@app.route('/categories/<int:user_id>', methods=['GET'])
def get_categories(user_id):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM category WHERE user_id = ?', (user_id,))
    categories = cursor.fetchall()
    conn.close()

    category_list = []
    for category in categories:
        category_list.append({
            "category_id": category[0],
            "category_name": category[1],
            "duration": category[2]
        })

    return jsonify(category_list), 200


# 강의 조회 함수
@app.route('/lectures/<int:category_id>', methods=['GET'])
def get_lectures(category_id):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM lecture WHERE category_id = ?', (category_id,))
    lectures = cursor.fetchall()
    conn.close()

    lecture_list = []
    for lecture in lectures:
        lecture_list.append({
            "lecture_id": lecture[0],
            "lecture_name": lecture[2],
            "duration": lecture[3]
        })

    return jsonify(lecture_list), 200


# 햘 일 조회 함수
@app.route('/todos/<int:lecture_id>', methods=['GET'])
def get_todos(lecture_id):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM to_do_list WHERE lecture_id = ?', (lecture_id,))
    todos = cursor.fetchall()
    conn.close()

    todo_list = []
    for todo in todos:
        todo_list.append({
            "to_do_list_id": todo[0],
            "date": todo[1],
            "achievement_or_not": bool(todo[2])
        })

    return jsonify(todo_list), 200



# 사용자 삭제 함수
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()

    if rows_affected == 0:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200


# 카테고리 삭제 함수
@app.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM category WHERE category_id = ?', (category_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()

    if rows_affected == 0:
        return jsonify({"message": "Category not found"}), 404
    return jsonify({"message": "Category deleted successfully"}), 200


# 강의 삭제 함수
@app.route('/lecture/<int:lecture_id>', methods=['DELETE'])
def delete_lecture(lecture_id):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM lecture WHERE lecture_id = ?', (lecture_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()

    if rows_affected == 0:
        return jsonify({"message": "Lecture not found"}), 404
    return jsonify({"message": "Lecture deleted successfully"}), 200


# 할 일 삭제 함수
@app.route('/todo/<int:to_do_list_id>', methods=['DELETE'])
def delete_todo(to_do_list_id):
    conn = sqlite3.connect('mbti_planner.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM to_do_list WHERE to_do_list_id = ?', (to_do_list_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()

    if rows_affected == 0:
        return jsonify({"message": "To-do item not found"}), 404
    return jsonify({"message": "To-do item deleted successfully"}), 200
