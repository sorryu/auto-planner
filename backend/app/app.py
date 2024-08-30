from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from response import Response

from temporary_database import Database, manageDatabase # 임시 데이터베이스

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jiseong1221'
jwt = JWTManager(app)

db = manageDatabase.generateDatabase()

# 사용자 로그인 엔드포인트
@app.route('/api/login', methods=['POST'])
def login():
    data:dict = request.get_json()
    """
    {
        "email": "user@email.com",
        "password": "bcrypt_password"
    }
    """
    if not data or 'email' not in data or 'password' not in data:
        response = Response(
            {
                "message": "Email and password are required"
            }, 400 #Bad Request
        )
    else:
        email = data.get('email')
        password = data.get('password')
        if email not in users or users[email] != password: # 패스워드 비교 및 해시화는 다른 모듈로 처리 예정
            response = Response(
                {
                    "message": "Invalid email or password"
                }, 401 #Unauthorized
            )
        else:
            access_token = create_access_token(identity=email)
            response = Response(
                {
                    "message": "Login Successful",
                    "access_token": access_token
                }, 200 #OK
            )
    return response.send()

# 사용자 회원가입 엔드포인트
@app.route('/api/signin', methods=['POST'])
def signin():
    data:dict = request.get_json()
    """
    {
        "name": "홍길동",
        "email": "user@email.com,
        "password": "bcrypt_password",
        "check_password": "bcrypt_password",
        "MBTI": "ABCD"
    }
    """
    if not data or ('name' and 'email' and 'password' and 'check_password' and 'MBTI') not in data:
        response = Response(
            {
                "message": "All elements are needed"
            }, 400 #Bad Request
        )
    else:
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        check_password = data.get('check_password')
        mbti = data.get('MBTI')
        if email in users:
            response = Response(
                {
                    "message": "Email already exists"
                }, 409 #Conflicts
            )
        elif password != check_password:
            response = Response(
                {
                    "message": "Password is Different"
                }, 401 #Unauthorized
            )
        else:
            users[email] = {
                "name": name,
                "password": password,
                "mbti": mbti
            }
            response = Response(
                {
                    "message": "User registered successfully"
                }, 200 #OK
            )
    return response.send()

# 날짜별 To-Do List 표시 엔드포인트
@app.route('/api/main/todos', methods=['GET'])
@jwt_required() # 로그인 필요
def get_todos():
    email = get_jwt_identity() # JWT에서 사용자 식별 정보를 가져온다.
    date = request.args.get('date')
    if not date:
        response = Response(
            {
                "message": "Invalid date format"
            }, 400 #Bad Request
        )
    else:
        user_todos:dict = todos.get(email, {})
        response = Response(
            {
                "todos": user_todos.get(date, [])
            }, 200 #OK
        )
    return response.send()

# 특정 날짜의 To-Do List 삭제 엔드포인트
@app.route('/api/main/todos', methods=['DELETE'])
@jwt_required()
def delete_todos():
    data:dict = request.get_json()
    """
    {
        "date": "yyyy-mm-dd",
        "todo": "title"
    }
    """
    if not data or 'date' not in data:
        response = Response(
            {
                "message": "Date is required"
            }, 400 #Bad Request
        )
    else:
        email = get_jwt_identity()
        date = data.get('date')
        todo = data.get('todo')
        user_todos = todos.get(email, {}).get(date, [])
        if todo in user_todos:
            del user_todos[todo]


# 특정 To-Do List를 완료 상태로 변경
@app.route('/api/main/todos', methods=['PATCH'])
def complete_todos():...

# 특정 카테고리 삭제
@app.route('/api/categories', methods=['DELETE'])
def delete_category():...

# 카테고리 추가
@app.route('/api/categories', methods=['POST'])
def add_category():...

# To-Do List 추가
@app.route('/api/plan', methods=['POST'])
def add_todo():...

# 추가한 카테고리로 계획 세우기
@app.route('/api/plan', methods=['POST'])
def make_plan():...

# 개인정보 변경하기
@app.route('/api/setting', methods=['PATCH'])
def edit_info():...