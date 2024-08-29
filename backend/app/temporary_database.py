import _userInfo
from _userInfo import User

class Database:
    def __init__(self, users:dict = None, categories = dict|None, todos = dict|None):
        self.users = {} or users
        self.categories = {} or categories
        self.todos = {} or todos

class createDatabase:
    @staticmethod
    def generateDatabase(**data):
        return Database(users=data.get('users', {}), categories=data.get('categories', {}), todos=data.get('todos', {}))