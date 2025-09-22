import math

def calculate_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * (radius ** 2)
    return round(area, 2)


print(calculate_area(5))  
