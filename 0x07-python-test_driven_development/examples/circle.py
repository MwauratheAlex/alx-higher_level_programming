from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError("r must be >= 0")
    if type(r) not in [int, float]:
        raise TypeError("r must be a positive real number")
    return pi*(r**2)
