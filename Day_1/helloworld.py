import math
#Basic Mathematical Operations
print(3 + 4)
print(3-4)
print(3*4)
print(3/4)
print(3**4)
print(3%4)
print(3//4)
print(4//3)

#Writing Strings
print("First name: Justin")
print('Last name: Hansen-Addy')
print("I am from Ghana")
print('I am doing 30 days of python')

#Checking Data Types
print(type(10))
print(type(9.5))
print(type("Hello, World!"))
print(type([1,2,3]))
print(type({'name':'Justin'}))
print(type({9.8, 3.14, 2.7})) 
print(type((9.8, 3.14, 2.7))) 

#Examples of Different Data Types in python
#Integer
print(377)
#Float
print(840.58)
#complex
print(4-4j)
#boolean
print(True)
#String
print('You are welcome')
#List
print([3, 6, 9, 12])
#Tuple
print((3, 6, 9, 12))
#Set
print({3, 6, 9, 12})    
#dictionary
print({'name':'Justin', 'country':'Ghana'})

#Finding an euclidean distance between two points
p1 = 2
p2 = 3
q1 = 10
q2 = 8
Distance = math.hypot(q1 - p1, q2 - p2)
print(f"{Distance:.2f}")