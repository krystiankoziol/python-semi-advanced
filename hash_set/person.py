from uuid import  uuid1

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.uuid = str(uuid1())

    def __eq__(self, other):
        return self.uuid == other.uuid

    def __hash__(self):
        return self.uuid = uuid1()

