import math

def polygon_area(n, s):
    
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area

n = int(input('Input number of sides: '))
s = int(input('Input the length of a side: '))
area = polygon_area(n, s)
print('The area of the polygon is:',round(area))
