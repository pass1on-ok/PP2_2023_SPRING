class Coor(object):
    def dist(x1, y1, x2, y2):
        return (((x2 - x1)**2 +(y2 - y1)**2)**0.5)
    def show(x1, y1, x2, y2):
        return (x1,y1,x2,y2)
x1 =int(input())
y1 =int(input())
x2 =int(input())
y2 =int(input())
print(show(x1,y1,x2,y2))
print(dist(x1,y1,x2,y2))
