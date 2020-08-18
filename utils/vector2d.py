class Vector2d:

    def __init__(self,x,y):
        self.x = x
        self.y = y


    def add(self, vector2d):
        return Vector2d(self.x+vector2d.x, self.y+vector2d.y)