from flask import jsonify

class Response:
    def __init__(self, json:dict, code:int) -> None:
        self.json = json
        self.code = code
    
    def send(self):
        return jsonify(self.json), self.code