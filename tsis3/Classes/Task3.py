class Shape:
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_area(self):
        return self.length * self.width

int1 = int(input())
int2 = int(input())
rect = Rectangle(int1,int2)
print(rect.get_area())
