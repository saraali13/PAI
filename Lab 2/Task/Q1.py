#A = ½ (a + b) h trapezoid
#A=bh parallelogram
#A = pi r square h  cylinder
import math

def trap_area(a, b):
    return (1/2)*(a + b)

def parallelogram_area(b, h):
    return b*h

def surf_volume(r, h):
    return math.pi * r*r*h

print(trap_area(8, 7))
print(parallelogram_area(9, 8))
print(surf_volume(5, 10))
