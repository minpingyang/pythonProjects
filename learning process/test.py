import math
# Define a function -- note the way you are meant to comment a function:
def multi_area(radius):
    """
    This function returns multiple values
    """
    temp = math.pi * radius**2
    return temp, 'other', 'return', 'values', 6

# Call the area function
print (multi_area(2)[0])

print (list(reversed(range(5,-10,1))))
    