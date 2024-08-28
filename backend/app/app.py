from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from response import Response

app = Flask(__name__)
jwt = JWTManager(app)

# 임시 데이터 저장소
users = []  # 사용자 목록

# 사용자 로그인 엔드포인트
@app.route('/api/login', methods=['POST'])
def login():
    data:dict = request.get_json()
    """
    {
        "email": "user@email.com"
        "password": "bcrypt_password"
    }
    """
    if not data or 'email' not in data or 'password' not in data:
        response = Response(
            {
                "message": "Email and password are required"
            }, 400
        )
    else:
        email = data.get('email')
        password = data.get('password')
        if email not in users or users[email] != password:
            response = Response(
                {
                    "message": "Invalid email or password"
                }, 401
            )
        else:
            response = Response(
                {
                    "message": "Login Successful"
                }, 200
            )
    return response.send()

# 사용자 회원가입 엔드포인트
@app.route('/api/signin', methods=['POST'])
def signin():...

# 날짜별 To-Do List 표시 엔드포인트
@app.route('/api/main/todos', methods=['GET'])
def get_todos():...

# 특정 날짜의 To-Do List 삭제 엔드포인트
@app.route('/api/main/todos', methods=['DELETE'])
def delete_todos():...

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