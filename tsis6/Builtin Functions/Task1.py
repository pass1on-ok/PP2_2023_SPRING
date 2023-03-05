from functools import reduce

def multiply(numbers):
    return reduce(lambda x, y: x*y, numbers)

numbers = list(map(int,input().split()))
result = multiply(numbers)

print("Result:", result)
