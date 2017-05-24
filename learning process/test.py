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

first = 'Bob'
print(first*4)
print ('hello,\n world!')
print ('hello,\t\t world!')
n = 10
while (n > 0): 
    print (n)
    if n == 9:
        break
    n = n - 1
print ("Blastoff!?")
n = 6
for i in range(n):
    print (i)