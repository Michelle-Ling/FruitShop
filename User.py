class User:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
        self.loggedIn = False

    def getId(self):
        return self.id
    
