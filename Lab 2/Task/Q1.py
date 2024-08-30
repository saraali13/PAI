import math

def trap_area(a, b):
    return (1/2)*(a + b)

def parallelogram_area(b, h):
    return b*h

def surf_volume(r, h):
    return math.pi * r*r*h

print("Area is: ",trap_area(5, 3))
print("Parallelogram is: ",parallelogram_area(4.5, 8))
print("Surface Volume is: ",surf_volume(7, 9.7))
