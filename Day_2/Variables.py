#Day2: 30 Days of Python
# Variables in Python

first_name = 'Justin'
last_name = 'Hansen-Addy'
full_name = first_name + ' ' + last_name
#full_name = f"{first_name} {last_name}" #this is another method called f-string
country = 'Ghana'
city = 'Accra'
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = True

#Declaring multiple variables in one line
school, course, year = 'KNUST', 'Computer Engineering', '3rd Year'

#Checking Data Types of Variables
print(type(first_name), type(last_name), type(full_name), type(country), type(city), type(age), type(year), type(is_married), type(is_true), type(is_light_on))

#Checking the length of variables
print(len(first_name), 'and', len(full_name))

#comparing the legth of variables
print(f"The length of my first name is {len(first_name)} while the length of my last name is {len(last_name)}")

print(f"My name is {full_name}, a {age} year old from {country}, based in {city}.")
print('Year: ', year)
print('Marriage Status: ', is_married)

#Some math using stated variable
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print('The sum of 5 and 4  is ', total)
print('The product of 5 and 4  is ', product)
print('The number 4 subtracted from 5 is ', diff)
print('5 divided by 4 is ', division)
print('When you divide 5 by 4 you get a remainder of ', remainder)
print('5 raise to the power 4 is ', exp)
print('When you divide 5 by 4 the nearest whole number is ', floor_division)

#More Math
radius_1 = 30
area_of_circle_1 = 3.14 * (radius_1**2)
circum_of_circle_1 = 2 * 3.14 * radius_1
print(f"The area of a circle with a radius of 30m is {area_of_circle_1} and it's circumference is {circum_of_circle_1}.")

#Asking for inputs
radius_2 = float(input('Enter radius here:'))
area_of_circle_2 = 3.14 * (radius_2**2)
circum_of_circle_2 = 2 * 3.14 * radius_2
print(f"The area of a circle with a radius of {radius_2}m is {area_of_circle_2} and it's circumference is {circum_of_circle_2}.")

#To avoid repetition that was done at the top I can use functions
"""def calculate_circle(r)
       area = 3.14 * (r**2)
       circumference = 2 * 3.14 * r
      
   radius_1 = 30
   calculate_circle(radius_1)
   
   radius_2 = float(input('Enter radius here: '))
   calculate_circle(radius_2)"""

First_name = input('Enter your first name here: ')
Last_name = input('Enter your last name here: ')
Full_name = First_name + ' ' + Last_name
Country = input('Enter your country here: ')
Age = input('Enter your age here: ')
print(f"My name is {Full_name}. I am {Age} and I am from {Country}.")