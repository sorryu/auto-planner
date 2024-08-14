from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YesJiseongTeam'
app.config['BCRYPT_LEVEL'] = 10
bcrypt = Bcrypt(app)

#UserInfo Class
class User():
    is_encrypt = False
    def __init__(self, id, password, name, mbti) -> None:
        self.id = id
        # Hash password using bcrypt
        self.password = bcrypt.generate_password_hash(password)
        self.name = name
        self.mbti = mbti


# What I have to do
# encrypting User class using base64
