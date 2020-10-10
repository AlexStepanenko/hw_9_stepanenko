import json


class Persons:
    def __init__(self, path):
        config = json.loads(open(path).read())
        self.name = config['name']
        self.age = config['age']
        self.gender = config['gender']

    def greet(self):
        message = f'Hello, my name is {self.name}.'
        return message
