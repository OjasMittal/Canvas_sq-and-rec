class Rectangle:
    def __init__(self,x,y,height,width,colour):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.colour=colour
    def draw(self,canvas):
        canvas.data[self.x:self.x+self.height,self.y:self.y+self.width]=self.colour


class Square:
    def __init__(self,x,y,side,colour):
        self.x=x
        self.y=y
        self.side=side
        self.colour=colour
    def draw(self,canvas):
        canvas.data[self.x:self.x + self.side, self.y:self.y + self.side] = self.colour