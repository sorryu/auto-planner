from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # JWT 시크릿 키 설정

jwt = JWTManager(app)

# 임시 데이터 저장소
users = []  # 사용자 목록

# Plan_list
# 계획 리스트
plan_list = []

# To do list
to_do_list = []

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


@app.route('/api/study-plans/edit-plans', methods=['POST'])
def editing_plans():
    data_of_plan = request.get_json()
    class_name = data_of_plan.get('class_name')
    plan_date = data_of_plan.get('plan_date') # '00.00.00 ~ 00.00.00'
    start_date = plan_date[0:8]
    end_date = end_date[-8:]
    period = 0
    # 기간을 구하는 알고리즘 제작
    unit_name = data_of_plan.get('unit_name') # 여러 개를 입력받는 방법 공부 필요
    expected_time = data_of_plan.get('expected_time')
    
    plan_id = len(plan_list) + 1

    plan = {
        'plan_id':plan_id,
        'class_name':class_name,
        'date':{
            'start_date':start_date,
            'end_date':end_date
        },
        'period':period,
        'unit': {
            unit_name:expected_time
        }
    }

    plan_list.append(plan)

    return 201

@app.route('api/study-plans/edit-to-do-list', methods=['POST'])
def editing_to_do_list():
    data_of_to_do_list = request.get_json()
    to_do_name = data_of_to_do_list.get('to_do_name')
    description = data_of_to_do_list.get('description')
    to_do_date = data_of_to_do_list.get('to_do_date')

    to_do_list_id = len(to_do_list) + 1

    to_do = {
        'to_do_list_id':to_do_list_id,
        'to_do_name':to_do_name,
        'description':description,
        'to_do_date':to_do_date
    }

    to_do_list.append(to_do)

    return 201


if __name__ == '__main__':
    app.run(debug=True)  # Flask 앱 실행
