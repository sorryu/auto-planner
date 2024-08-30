"""
_todoInfo.py

class Todo: {
    attribute: [title, category]
    methods: []
}
"""

class Todo:
    completed = False
    def __init__(self, title:str, category:str, date:str):
        self.title = title
        self.category = category
        self.date = date
    
    def __eq__(self, value: 'Todo') -> bool:
        return self.title == value.title and self.category == value.category

class ManageTodo:
    @staticmethod
    def generateTodo(title:str, category:str, date:str) -> Todo:
        return Todo(title, category, date)
    
    @staticmethod
    def completeTodo(todo:Todo) -> bool:
        todo.completed = True
        return todo.completed
    
    @staticmethod
    def deleteTodo(todo:Todo) -> bool:
        del todo
        return True