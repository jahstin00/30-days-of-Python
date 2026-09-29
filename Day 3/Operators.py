import math
#Using assignment operators to declare variables
Age = 20
Height = 179.8
comp = 4-2j
b = float(input('Enter base of triangle here: '))
h = float(input('Enter height of triangle here: '))
area_t = 0.5 * b * h #using arithmetic operator to find area of a triangle 
print('The area of your triangle is ', area_t)

#Finding perimeter of triangle
xs = float(input('Enter first side here: '))
ys = float(input('Enter second side here: '))
zs = float(input('Enter third side here: '))
perimeter_t = xs + ys + zs
print('The perimeter of your triangle is ', perimeter_t)

#Finding area and perimeter of a rectangle
length = float(input('Enter length of rectangle here: '))
width = float(input('Enter width of rectangle here: '))
area_r = length * width
perimeter_r = 2*(length+width)
print('Area of your rectangle is ', area_r)
print('Perimeter of your rectangle is ', perimeter_r)

#Finding area and circumference of a circle
pi = 3.14
r = float(input('Enter the radius of your circle here: '))
area_c = pi * (r**2)
circumference = 2 * pi * r
print(f"The area of your circle is {area_c} and its circumference is {circumference}")

# Getting properties of a line
def line_properties(m,b):
    slope = m
    y_intercept = b
    if m == 0:
        x_intercept = None
    else:
        x_intercept = -b/m
    return slope, y_intercept, x_intercept

m_value = 2
b_value = -2

slope, y_int, x_int = line_properties(m_value,b_value)
print(f"Slope is {slope}")
print(f"Y-intercept is {y_int}")
print(f"X-intercept is {x_int}")

#Finding slope and Euclidean distance between points
y1, y2 = float(input('y1: ')), float(input('y2: '))
x1, x2 = float(input('x1: ')), float(input('x2: '))
m_slope = (y2-y1)/(x2-x1)
Distance = math.hypot(x2-x1, y2-y1)
print(f"The slope between the two points is {m_slope}")
print(f"The euclidean distance between the point is {Distance:.2f}")

#Comparing the first slope to the second slope in both scenarios
print('The first and second slope are the same: ', slope is m_slope)
print('The first is greater than the second slope: ', slope > m_slope)
print('The first and second slope are the same: ', slope == m_slope) #using the equivalent operator

#Given a certain equation and making sure a condition is met
target = 0
x = 0
y = x**2 + 6*x + 9
print('The given equation is (y = x^2 + 6x + 9)')
print(f"Starting value: {x} but y is not 0")
while y != target:
    x -= 1
    y = x**2 + 6*x + 9
    print(f"The current reduced value of x is {x}, and its y value is {y}")

print(f"\nDone. Hence the value of x that makes y = 0 is {x}")

#Finding the length of some words and making comparison
w1 = 'python'
w2 = 'dragon'
print(f"The length of the word python is {len(w1)} and that of dragon is {len(w2)}")
print(f"The two words are the same: {w1 == w2}")

#Checking if a letter is in two words using 'and'
print('Is (on) in python and dragon: ', 'on' in (w1  and w2))

#Checking if a word is in a sentence 
sent = 'I hope this course is not full of jargon'
print('Is the word jargon is in (I hope this course is not full of jargon): ', 'jargon' in sent)
print('There is no (on) in both dragon and python: ', 'on' in (w1  and w2))

#converting Data types
w3 = len(w1)
w4 = float(w3)
w5 = str(w3)
print(f"python: {w3}, {w4}, and {w5}")

#Checking if a number is even
num = float(input('Enter number here:'))
eqn = num % 2
if eqn == 0:
    print(f"{num} is even")
else:
    print(f"{num} is not even")

#Checking if the floor division of 7 by 3 is equal to the int converted value of 2.7.
res_1 = 7//3
num_1 = 2.7
res_2 = int(num_1)
print('Is the floor division of 7 by 3 is equal to the int converted value of 2.7: ', res_1 == res_2)

#Checking if type of '10' is equal to type of 10
var_1 = '10'
var_2 = 10
print('Is type of 10(with quotes on it)  equal to type of 10(without quotes): ', type(var_1) == type(var_2))

#Checking if int('9.8') is equal to 10
var_3 = '9.8'
var_4 = int(float(var_3))
var_5 = 10
print(f"Is int('9.8') equal to 10: {var_4 == var_5}")

#Calculating pay of a person
hours = float(input('Enter hours per week here: '))
rate = float(input('Enter rate per hour here: '))
pay = hours * rate
print(f"Your weekly pay is ${pay}")

#Calculating the number of seconds a person has lived per year
years = float(input('Enter the number of years you have lived: '))
sec_per_yr = 31536000
num_sec = years * sec_per_yr
print(f"You have lived for {num_sec} seconds")

#Creating a table
print('TABLE')
for n in range(1, 6):
    print(f"{n} 1 {n} {n**2} {n**3}")
