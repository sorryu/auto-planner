from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # JWT 시크릿 키 설정
app.config['SECRET_KEY'] = 'YesJiseongTeam'
app.config['BCRYPT_LEVEL'] = 10
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# 임시 데이터 저장소
users = []  # 사용자 목록

# 사용자가 로그인하지 않은 상태인지 확인하는 엔드포인트
@app.route('/api/study-plans/home', methods=['HEAD'])
def check_not_logged_in():
    return '', 401  # 항상 401 Unauthorized 반환

# 사용자가 로그인한 상태인지 확인하는 엔드포인트
@app.route('/api/study-plans/home/<int:user_id>', methods=['HEAD'])
@jwt_required()  # JWT 인증 필요
def check_logged_in(user_id):
    return '', 200  # 항상 200 OK 반환

# 사용자 로그인 엔드포인트
@app.route('/api/study-plans/login', methods=['POST'])
def login():
    data = request.get_json()  # 요청에서 JSON 데이터 추출
    email = data.get('email')  # 이메일 추출
    password = data.get('password')  # 비밀번호 추출
    
    # 이메일과 비밀번호가 일치하는 사용자를 찾음
    user = next((u for u in users if u['login_info']['Email'] == email and u['login_info']['password'] == password), None)
    
    if user:
        access_token = create_access_token(identity=user['user_id'])  # JWT 액세스 토큰 생성
        return jsonify(token=access_token, user_id=user['user_id']), 200  # 토큰과 사용자 ID 반환
    else:
        return jsonify({"msg": "Bad email or password"}), 401  # 로그인 실패 시 401 Unauthorized 반환

# 새로운 사용자 회원가입 엔드포인트
@app.route('/api/study-plans/signup', methods=['POST'])
def signup():
    data = request.get_json()  # 요청에서 JSON 데이터 추출
    email = data.get('email')  # 이메일 추출
    password = data.get('password')  # 비밀번호 추출
    pw_hash = bcrypt.generate_password_hash(password)
    name = data.get('name')  # 이름 추출
    mbti = data.get('mbti')  # MBTI 추출
    
    # 이미 존재하는 이메일인지 확인
    if any(u for u in users if u['login_info']['Email'] == email):
        return jsonify({"error": "Email already exists"}), 400  # 이메일이 이미 존재하면 400 Bad Request 반환

    user_id = len(users) + 1  # 새로운 사용자 ID 생성
    user = {
        "user_id": user_id,
        "login_info": {"Email": email, "password": password},
        "user_info": {"name": name, "mbti": mbti}
    }
    users.append(user)  # 사용자 목록에 추가
    return jsonify(user_id=user_id), 201  # 새로운 사용자 ID 반환

if __name__ == '__main__':
    app.run(debug=True)  # Flask 앱 실행
