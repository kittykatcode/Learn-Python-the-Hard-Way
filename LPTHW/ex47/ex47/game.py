class Room(object):
    def __init__(self,name,describtion):
        self.name = name
        self.describtion = describtion
        self.path = {}

    def go(self,direction):
        return self.path.get(direction,None)

    def add_path(self,path):
        self.path.update(path)
