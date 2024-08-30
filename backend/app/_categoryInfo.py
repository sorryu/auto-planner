"""
_categoryInfo.py

class Category:
    attribute: [userid, title, category]
    methods: []
"""

import time

from _userInfo import ID

class Category:
    def __init__(self, title, startdate, duedate, lectures:dict = {}):
        self.title = title
        self.start = startdate
        self.end = duedate
        self.lectures = lectures

class Lecture:
    def __init__(self, title, category:str, expected_time:str, id:None|str) -> None:
        self.title = title
        self.category = category
        self.expected_time = expected_time # 시간 및 날짜 관리 모듈 만들어야 함.
        self.id = id or str(int(time.time()))

class ManageCategory:
    @staticmethod
    def generateCategory(title, startdate, duedate) -> Category:
        return Category(title, startdate, duedate)
    
    @staticmethod
    def deleteCategory(category:Category):
        del category
        return True
    
    @staticmethod
    def generateLecture(title, category:str, expected_time:str):
        return Lecture(title, category, expected_time)
    
    @staticmethod
    def deleteLecture(category:Category, lecture:Lecture):
        del category.lectures[lecture.id]
        return True