"""
_userInfo.py

Class User: {
    attribute: [is_encrypt, email, name, mbti, password, id],
    methods: [__init__, hashing, encode_info, decode_info, change_password, patch_user_info, compare_user_info, generate_id]
}
"""

from flask import Flask
from flask_bcrypt import Bcrypt
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YesJiseongTeam'
app.config['BCRYPT_LEVEL'] = 10
bcrypt = Bcrypt(app)

import time
import uuid
import hashlib

class ID:
    def __init__(self, id: str = None) -> None:
        self.id = id or self.generate_id()

    @staticmethod
    def generate_id() -> 'ID':
        """
        Generate a unique user ID combining timestamp and a hashed UUID.
        Return an ID object.
        """
        timestamp = int(time.time())  # 현재 타임스탬프
        random_uuid = str(uuid.uuid4())  # 무작위 UUID4 생성
        hashed_uuid = hashlib.sha256(random_uuid.encode('utf-8')).hexdigest()
        return ID(f"{timestamp}-{hashed_uuid}")

    def __eq__(self, other) -> bool:
        """
        Compare two ID objects by their id values.
        """
        if isinstance(other, ID):
            return self.id == other.id
        return False

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return f"ID({self.id})"

class User:
    is_encrypt = False  # 'is_encrypt' variable checks if the user information is encoded or not.

    def __init__(self, email: str, password: str, name: str, mbti: str, id: ID = None) -> None:
        """
        Initialize the user with email, password, name, and mbti.
        Generate a unique ID if not provided.
        """
        self.email = email
        self.name = name
        self.mbti = mbti
        self.password = self.hashing(password)
        self.id = id or ID.generate_id()
        self.encode_info()

    def hashing(self, password: str) -> str:
        """
        Hash the password using bcrypt.
        """
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def encode_info(self) -> bool:
        """
        Encoding the variables excluding password.
        """
        if self.is_encrypt:
            return False

        self.email = base64.b64encode(self.email.encode('utf-8')).decode("utf-8")
        self.name = base64.b64encode(self.name.encode('utf-8')).decode("utf-8")
        self.mbti = base64.b64encode(self.mbti.encode('utf-8')).decode("utf-8")

        self.is_encrypt = True
        return self.is_encrypt

    def decode_info(self) -> bool:
        """
        Decode the encrypted information.
        """
        if not self.is_encrypt:
            return False
        
        self.email = base64.b64decode(self.email.encode('utf-8')).decode("utf-8")
        self.name = base64.b64decode(self.name.encode('utf-8')).decode("utf-8")
        self.mbti = base64.b64decode(self.mbti.encode('utf-8')).decode("utf-8")
        
        self.is_encrypt = False
        return True

    def change_password(self, new_password: str) -> bool:
        """
        Change the user's password.
        """
        self.password = self.hashing(new_password)
        return True

    def patch_user_info(self, email: str, name: str, mbti: str, password: str) -> bool:
        """
        Update user information and re-encode it.
        """
        self.email = email
        self.name = name
        self.mbti = mbti
        self.change_password(password)
        return self.encode_info()

    def update_user_info(self, **kwargs) -> bool:
        """
        Compare the provided user info with the current instance.
        Update the information if they differ, and return True if any changes were made.
        """
        self.decode_info()
        updated = False
        if self.email != kwargs.get('email'):
            self.email = kwargs.get('email')
            updated = True
        if self.name != kwargs.get('name'):
            self.name = kwargs.get('name')
            updated = True
        if self.mbti != kwargs.get('mbti'):
            self.mbti = kwargs.get('mbti')
            updated = True
        
        if updated:
            self.encode_info()
        return updated

if __name__ == "__main__":
    example = User("ybin039@khu.ac.kr", "Yubin", "Jeon Yubin", "INFJ")