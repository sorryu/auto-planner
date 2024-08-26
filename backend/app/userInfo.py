from flask import Flask
from flask_bcrypt import Bcrypt
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YesJiseongTeam'
app.config['BCRYPT_LEVEL'] = 10
bcrypt = Bcrypt(app)

# The Class of User Information
# 유저 정보 클래스
class User():
    # 'is_encrypt' variable plays a role in 
    # checking if user information is encoded or not.
    # 'is_encrypt' 변수는 유저 정보가 암호화 여부를 확인하는 역할임.

    # If you don't make a function of checking encoding or decoding in this class,
    # the position of it will be changed.
    # 만약 이 클래스에서 암호화 여부를 확인하지 않는다면, 위치를 변경해야 함.


    is_encrypt = False

    # User Information variables (유저 정보 변수)
    def __init__(self, id: str, password: str, name: str, mbti: str) -> None:
        self.id = id
        self.name = name
        self.mbti = mbti

        # Saving hashed password directly using bcrypt
        # bcrypt로 해시된 비밀번호를 바로 저장함.
        self.password = bcrypt.generate_password_hash(password)
        
    # encrypting User class using base64 (base64를 이용한 유저 클래스 암호화)
    
    '''
    def encode_info(self):
        # Encoding the variables excluding password. 
        # 비밀번호를 제외한 변수들을 암호화함. 

        # First, the variables to encode are changed to byte type
        # (Because the function of base64 can't encode str type, but they are string type)
        # 첫 번째, 암호화할 변수를 byte 타입으로 변환함. 
        # (왜냐하면 str 타입은 base64의 함수로 암호화가 불가능한데, 이 변수들은 str 타입임.)

        byte_id = self.id.encode('utf-8')
        byte_name = self.name.encode('utf-8')
        byte_mbti = self.mbti.encode('utf-8')

        # Second, the byte types are encoded using base64
        # 두 번째, base64로 바이트 타입이 암호화됨.
        encoded_id = base64.b64encode(byte_id)
        encoded_name = base64.b64encode(byte_name)
        encoded_mbti = base64.b64encode(byte_mbti)

        print(self.id, self.name, self.mbti)
        print(encoded_id, encoded_name, encoded_mbti)
    '''
        
    # This function changes password and rehashs it.
    # 새로 받은 패스워드를 입력받아 변경하고, 해시화해 저장함.
    def change_pw(self,new_pw):
        self.password = bcrypt.generate_password_hash(new_pw)

    # This function changes mbti
    def change_mbti(self,now_mbti):
        self.mbti = now_mbti

        # self.encode_info() 
        # This code is changed after we reapply the encoding function.
        # 암호화 다시 적용 후 변경 예정


example = User("ybin039@khu.ac.kr", "Yubin", "Jeon Yubin", "INFJ")