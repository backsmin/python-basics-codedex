import math

# User chooses which shape's area to calculate
shape = input(
    'Which shape\'s area would you like to calculate ? \n 1. Square \n 2. Rectangle \n 3. Triangle \n 4. Circle \n ')

# Conditionals to determine the shape's are by user's choice
# 1. Square
if shape == '1' or shape == '1.':
    side = float(
        input('Enter the side\'s length: '))
    area = side**2
    print(f'Area of the square is {area}.')

# 2. Rectangle
elif shape == '2' or shape == '2.':
    length = float(
        input('Enter the length: '))
    width = float(
        input('Enter the width: '))
    area = length * width
    print(f'Area of the rectangle is {area}.')

# 3. Triangle
elif shape == '3' or shape == '3':
    height = float(
        input('Enter the height: '))
    base = float(input('Enter the base: '))
    area = (height * base) / 2
    print(f'Area of the triangle is {area}.')


# 4. Circle
elif shape == '4' or shape == '4':
    radius = float(input('Enter the radius: '))
    area = math.pi * radius**2
    print(f'Area of the circle is {area}.')

else:
    print('Invalid shape.')
