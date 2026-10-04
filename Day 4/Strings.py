#Concatenation
"""First = 'Justin'
Last = 'Addy'
Space = ' '
Full = First + Space .join(Last)
print(Full)
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
#String Formatting
'''%s - String (or any object with a string representation, like numbers)
   %d - Integers
   %f - Floating point numbers
   "%.number of digitsf" - Floating point numbers with fixed precision'''
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formatted_string = 'The following are python libraries:%s' %(python_libraries)
print(formatted_string)
a =4
b = 7
first = '{} + {} = {}'.format(a,b,a+b)
second = '%d + %d = %d' %(a,b,a+b)
print(first)
print(second)
food = 'jollof'
a,b,c,d,e,f = food
first_letter = food[0]
last_letter = food[-1]
first_2 = food[0:2]
last_2 = food[-2:]
jl = food[0:7:3]
lf = food[2:7:3]
sub_string = 'o'
print(food.rindex(sub_string))
print(food.count('o',0,3))
print(food.capitalize())
print(lf)
print(jl)
print(food[::-1])
print(last_2) 
print(first_2)
print(last_letter)
print(first_letter)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)"""

#Concatenation
first_word = 'Thirty'
sec_word = 'Days'
third_word = 'Of'
last_word = 'Python'
space = ' '
full_sentence = first_word + space + sec_word + space + third_word + space + last_word
print(full_sentence)
phrase = ['Coding', 'For', 'All']
comp_phrase = space.join(phrase)
print(comp_phrase)
print(len(comp_phrase))
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
no_coding = company[7:]
print(no_coding)
print(company.find('Coding'))
print(company.count('Coding'))
print(company.index('Coding'))
print(company.startswith('Coding'))
print(company.replace('Coding', 'Python'))
orig = 'Python For Everyone'
print(orig.replace('Everyone', 'All'))
print(company.split(space))
socials = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(socials.split(', '))
first_letter = company[0]
print(first_letter)
print(company.rindex('l'))
print(company[10])
PFr = orig[0:20:7]
CF =company[0:14:7]
print(PFr)
print(CF)
print(company.index('C'))
print(company.index('F'))
New = company + space + 'People'
print(New.rfind('l'))

#Finding the first occurrence of a word in a sentence using find() and index()
new_sent = 'You cannot end a sentence with because because because is a conjunction'
print(new_sent.index('because'))
print(new_sent.find('because'))
#Now we are using rindex to find the last occurrence
print(new_sent.rfind('because'))
slice_because = new_sent[31:54] #slicing a phrase out of the sentence
print(slice_because)
print(company.startswith('Coding')) #Checking if a string starts with a certain substring
print(company.endswith('coding')) #Checking if a string ends with a certain substring

#Removing some character from a string
old = '   Coding For All      '
print(old.strip('      '))
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

#Joining a list with certain characters
my_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
add_hash = '# '
new_list = add_hash.join(my_list)
print(new_list)

#Using the new line escape sequence to separate the following sentences
ff_sent = 'I am enjoying this challenge.\nI just wonder what is next.'
print(ff_sent)

#Use a tab escape sequence to write the following lines
tt_sent = 'Name\tAge\tCountry\tCity\nJustin\t20\tGhana\tAccra'
print(tt_sent)

#Using the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

a = 8
b = 6
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} x {} = {}'.format(a, b, a*b))
print('{} / {} = {}'.format(a, b, a/b))
print('{} mod {} = {}'.format(a, b, a%b))
print('{} // {} = {}'.format(a, b, a//b))
print('{} ^ {} = {}'.format(a, b, a**b))