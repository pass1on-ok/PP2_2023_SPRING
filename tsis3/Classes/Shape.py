class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

integer = int(input())
Asqr = Square(integer)
print(Asqr.area())      

print(Square().area())  
