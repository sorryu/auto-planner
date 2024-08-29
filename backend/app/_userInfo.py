"""
_userInfo.py

Class User: {
    attribute: [is_encrypt, email, name, mbti, password],
    methods: [__init__, hashing, encode_info, decode_info, change_password, patch_user_info, compare_user_info, generate_id]
}
"""

from flask import Flask
from flask_bcrypt import Bcrypt
import base64

import time # 고유 id 생성에 필요
import uuid # 고유 id 생성에 필요
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YesJiseongTeam'
app.config['BCRYPT_LEVEL'] = 10
bcrypt = Bcrypt(app)

class User():
    is_encrypt = False # 'is_encrypt' variable checks if the user informations are encoded or not.

    # 초기화
    def __init__(self, email: str, password: str, name: str, mbti: str, id:str|None) -> None:
        """
        Save hashed password directly using bcrypt
        """
        self.email = email
        self.name = name
        self.mbti = mbti
        self.password = self.hashing(password)
        self.encode_info()

        self.id = id or self.generate_id()

    # 비밀번호 해시화
    def hashing(self, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        return hashed_password

    # 암호화
    def encode_info(self) -> bool:
        """
        Encoding the variables excluding password.
        """
        if self.is_encrypt == True:
            return False

        self.email = base64.b64encode(self.email.encode('utf-8')).decode("utf-8")
        self.name = base64.b64encode(self.name.encode('utf-8')).decode("utf-8")
        self.mbti = base64.b64encode(self.mbti.encode('utf-8')).decode("utf-8")

        # 암호화 여부 변경
        self.is_encrypt = True
        return self.is_encrypt

    # 복호화
    def decode_info(self) -> bool:
        if self.is_encrypt == False:
            return self.is_encrypt
        
        self.email = base64.b64decode(self.email.encode('utf-8')).decode("utf-8")
        self.name = base64.b64decode(self.name.encode('utf-8')).decode("utf-8")
        self.mbti = base64.b64decode(self.mbti.encode('utf-8')).decode("utf-8")
        
        self.is_encrypt = False
        return True

    # 비밀번호 변경
    def change_password(self, new_password) -> bool:
        self.password = self.hashing(new_password)
        return True

    # 유저 정보 변경
    def patch_user_info(self, email, name, mbti, password):
        self.email = email
        self.name = name
        self.mbti = mbti
        self.change_password(password)
        return self.encode_info()

    # 유저 정보 비교
    def update_user_info(self, **kwargs) -> bool:
        self.decode_info()
        if self.email == kwargs['email'] and self.name == kwargs['name'] and self.mbti == kwargs['mbti']:
            return False
        if self.email != kwargs['email']:
            self.email = kwargs['email']
        if self.name != kwargs['name']:
            self.name = kwargs['name']
        if self.mbti != kwargs['mbti']:
            self.mbti = kwargs['mbti']
        
        self.encode_info()
        return True
    
    # 유저 고유 id 생성
    @staticmethod
    def generate_id() -> str:
        timestamp = int(time.time()) # 현재 타임스탬프
        random_uuid = str(uuid.uuid4()) # 무작위 uuid4 생성

        hashed_uuid = hashlib.sha256(random_uuid.encode('utf-8')).hexdigest()

        id = f"{timestamp}-{hashed_uuid}"
        return id

if __name__ == "__main__":
    example = User("ybin039@khu.ac.kr", "Yubin", "Jeon Yubin", "INFJ")