def parallelogram_area(l, h):
    
    area = l * h
    return float(area)

l = int(input('Length of base: '))
h = int(input('Height of parallelogram: '))
area = parallelogram_area(l, h)
print('Expected Output:',area)
