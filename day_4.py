#Creating a string multiline
# Using triple single quotes
multiline_single= ''' Working on code '''
multiline_double= """ Another manner of declaring a string """
#Concatenation of strings
combine_strings= multiline_single + multiline_double
print(combine_strings)
print(len(combine_strings))
#Formatting and Escape sequences
print("Days\t Topics")
print("Day 1\t5 \t5")
name="erika"
lname="dominic"
animal="cat"
formatted_string= 'In a movie character %s %s has a %s that is cute.' %(name, lname, animal)
print(formatted_string)

#Strings and numbers
rad=10
pi=3.14
a=pi* rad**2
formatted_string='The area of circle with a radius %d is %.2f' %(rad, a)
print(formatted_string)

#List and strings
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formatted_string= 'The following are python libraries:%s' %(python_libraries)
print(formatted_string)

#Usage of {} and format method
a, b= 4, 5
print('{} + {} = {}' .format(a, b, a+b))
print('{} - {} = {}' .format(a, b, a-b))
print('{} * {} = {}' .format(a, b, a*b))
# Usage of {} and format method using 2float point
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(rad, a) # 2 digits after decimal
print(formated_string)
#Python f-strings (formatted string literals)
print(f'{a} / {b} = {a / b: .2f}') 
print(f'{a} % {b} = {a  % b}')

#Strings as sequences of characters
lang='python'
l,m,n,o,p,q= lang
print(l)
print(m)
print(n)
print(o)
print(p)
print(q)
initial= lang[0]
print(initial)

#Slicing String
#Generic Syntax [start:stop:step]
#Step means increment
language= 'Python'
first_three= language[0:3]
print(first_three)

#Reversing a string
#Negative index means we are accessing from right instead of left
print(language[::-1])

#Skipping characters while slicing
#Start=0, stop=6 and step=2
#Begins at iniital and stops at index 5
#Skips every other item by moving 2 increments
skip_character= language[0:6:2]
print(skip_character)

