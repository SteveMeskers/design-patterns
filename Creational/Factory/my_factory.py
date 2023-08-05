class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    id = -1
    
    def create_person(self, name):
        self.id += 1
        return Person(self.id, name)
        