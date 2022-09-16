# x=int(input('gtri x='))
# y=int(input('gtri y ='))

# def compare():
#     if x>y:
#         return 1
#     elif x == y:
#         return 0
#     else:
#         return -1

# print(compare())
import math
from cmath import sqrt


def distance (x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result= math.sqrt(dsquared)
    return result

print (distance(1,1,4,5))




