"""
temporary_database.py
임시 저장소

class Database: {
    attribute: [users, categories, todos]
}

class manageDatabase: {
    method: [generateDatabase, is_conflicts, addUser, patchUser,
        addCategory, deleteCategory, addLecture, deleteLecture, 
        addTodo, completeTodo]
}
"""

import _userInfo, _categoryInfo, _todoInfo
from _userInfo import ID, User
from _categoryInfo import Category, Lecture, ManageCategory
from _todoInfo import Todo, ManageTodo

class Database:
    def __init__(self, users:dict, categories:dict, todos:dict):
        self.users = users
        self.categories = categories
        self.todos = todos

class manageDatabase:
    @staticmethod
    def generateDatabase(**data):
        return Database(users=data.get('users', {}), categories=data.get('categories', {}), todos=data.get('todos', {}))
    
    @staticmethod
    def is_conflicts(database:Database, userid:ID, categoryTitle:str = None, todoDate:str = None, todoTitle:str = None, check:str = "user"):
        """check = ['user'/'category'/'todo']"""
        match check:
            case 'user':
                if userid in database.users:
                    return True
            case 'category':
                if categoryTitle in database.categories.get(userid, {}):
                    return True
            case 'todo':
                if todoTitle in database.todos.get(userid, {}).get(todoDate):
                    return True
        return False


    @staticmethod
    def addUser(database:Database, email, password, name, mbti):
        user = User(email, password, name, mbti) # id는 자동생성
        database.users[user.id] = user
        return True
    
    @staticmethod
    def patchUser(database:Database, userid:ID, new_email = None, new_password = None, new_name = None, new_mbti = None):
        if not manageDatabase.is_conflicts(database, userid, check='user'):
            return False
        database.users[userid].email = new_email or database.users[userid].email
        database.users[userid].password = new_password or database.users[userid].password
        database.users[userid].name = new_name or database.users[userid].name
        database.users[userid].mbti = new_mbti or database.users[userid].mbti

        return True
    
    def addCategory(database:Database, userid:ID, title, start, end):
        if not manageDatabase.is_conflicts(database, userid, categoryTitle=title, check='category'):
            category:Category = ManageCategory.generateCategory(title, start, end)
            if not userid in database.categories:
                database.categories[userid] = dict()
            database.categories[userid][title] = category
            return True
        return False
    
    def deleteCategory(database:Database, userid:ID, title:str):
        if not manageDatabase.is_conflicts(database, userid, categoryTitle=title, check='category'):
            return False
        ManageCategory.deleteCategory(database.categories[userid][title])
        del database.categories[userid][title]
        return True
    
    def addLecture(database:Database, userid:ID, categoryTitle:str, lectureTitle:str, expected_time:str):
       category:Category = database.categories[userid][categoryTitle]
       lecture = ManageCategory.generateLecture(lectureTitle, categoryTitle, expected_time)
       category.lectures[lecture.id] = lecture
       return True
    
    def deleteLecture(database:Database, userid:ID, categoryTitle:str, lectureId:str):
        category:Category = database.categories[userid][categoryTitle]
        lecture:Lecture = database.categories[userid][categoryTitle].get(lectureId)
        return ManageCategory.deleteLecture(category, lecture) #무조건 True 값 반환하는 메소드
    
    def addTodo(database:Database, userid:ID, title, category, date):
        if not manageDatabase.is_conflicts(database, userid, todoDate = date, todoTitle=title, check="todo"):
            todos:dict = database.todos[userid]
            todo = ManageTodo.generateTodo(title, category, date)
            if not todo.date in todos:
                todos[todo.date] = {}
            todos[todo.date][title] = todo
            return True
        return False
    
    def completeTodo(database:Database, userid:ID, date, title):
        if not manageDatabase.is_conflicts(database, userid, todoDate=date, todoTitle=title, check='todo'):
            return False
        todo:Todo = database.todos[userid][title]
        todo.completed = True
        return True
    