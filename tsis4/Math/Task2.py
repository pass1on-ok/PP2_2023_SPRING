def trapezoid_area(a, b, h):
    
    area = 0.5 * (a + b) * h
    return area

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

area = trapezoid_area(a, b, h)
print('Expected Output:',area)
