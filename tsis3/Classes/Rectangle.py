class Rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

int1 = int(input())
int2 = int(input())
rect = Rectangle(int1,int2)
print(rect.area())
