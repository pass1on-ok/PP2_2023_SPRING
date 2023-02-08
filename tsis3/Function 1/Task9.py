import math
def sphere_vol(r):
    V = (3/4) * math.pi * (r**3)
    return V

r = int(input())

print(sphere_vol(r))
