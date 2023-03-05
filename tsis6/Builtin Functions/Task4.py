import math
import time

def delayed_sqrt(x, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(x)

x = int(input("Enter a number to compute the square root of: "))
milliseconds = int(input("Enter the number of milliseconds to wait: "))

result = delayed_sqrt(x, milliseconds)

print("Square root of {x} after {milliseconds} milliseconds is {result}".format(x=x,milliseconds=milliseconds,result=result))
