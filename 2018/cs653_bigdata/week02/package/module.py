class Rectangle(object):
    def __init__(self,w=0,h=0):
        self.w=w
        self.h=h
    def __str__(self):
        return 'Rectangle, w:%s, h:%s, area:%s'\
            %(self.w, self.h,self.area() )
    def area(self):
        return self.w*self.h

class Square(Rectangle):
    def __init__(self,w):
        self.w=w
        self.h=w