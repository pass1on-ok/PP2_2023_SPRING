import math

def degree_to_radian(degrees):
   
    radians = math.radians(degrees)
    return round(radians, 6)


degrees = int(input('Input degree: '))
radians = degree_to_radian(degrees)
print('Output radian:',radians)
