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

# String methods
#Capitalize= Makes initial capital
print(name.capitalize())
#Count= counts how many times a substring or a letter came in an argument
print("Number of times letter i came in:", lname.count('i'))
#Endswith= checks either the ending letters match the given argument or not
print("Does the name dominic end with ic letters: ", lname.endswith('ic'))
#Find= finds a substring, if nothing is found we get -1 as result
print(language.find('y'))
#rfind= returns the index of the substring that matches the argument
print(language.rfind('y'))
#index= returns the lowest index of a substring
challenge= "thirty two days to go"
sub_string='da'
print(challenge.index(sub_string))
#rindex= returns highest index of a substring
print(challenge.rindex(sub_string))
#isalnum= checks alphanumeric character
print(lname.isalnum())
#isalpha= checks if all are alphabets
print(lname.isalpha())
#isdecimal= checks if all characters are decimal (0-9)]
r='10'
print(r.isdecimal())
#is identifier= checks if a string is valid variable name
identify='23daysleft'
print(identify.isidentifier())
#islower checks if all alphabets are in lowercase
print(name.islower())
#isupper checks if all alphabets are in uppercase
print(name.isupper())
#join returns a concatenated string
web_tech=['html', 'css', 'js', 'reactjs']
outcome='Web ' .join(web_tech)
print(outcome)

#strip= removes all given characters from the start/ end of string
print('Removing "s" and "f" from string 23daysleft:' ,identify.strip('s') )
#replace=replace substring with a given string
print(challenge.replace('thirty', 'twenty'))
#split= splits the string using given string as a separator
print(challenge.split('thirty'))
#title returns the title cased string
print(challenge.title())
#swapcase= converts all uppercase to lowercase and lowercase to uppercase
print(multiline_double.swapcase())
#startswith= checks if string starts with specified string
print(multiline_double.startswith(" Another"))

#Exercise
w1= 'Thirty'
w2= 'Days'
w3= 'of'
w4= 'Python'
ws_combined= w1+ w2+ w3+ w4
print(ws_combined)

w1='Coding'
w2='For'
w3='All'
ws_combined=w1+w2+w3
print(ws_combined)

company='Coding for all'
print(company)
print("The length of text in variable company: ", len(company))
print("Result with using uppercase method: ", company.upper())
print("Result with lowercase method: ", company.lower())
print("Result with capitalize method: ", company.capitalize())
print("Result with title method: ", company.title())
print("Result with swapcase method: ", company.swapcase())
outcome=company[0:6]
print("Result of slice method:", outcome)
sub= "Coding"
print("Result of find method:", company.find(sub))
print("Result of index method:", company.index(sub))
print("Result of rfind method:", company.rfind(sub))
print("Result of rindex method:", company.rindex(sub))
result=company.replace('Coding', 'Python')
print("Result of replace method:", company.replace('Coding', 'Python'))
w="Python for Everyone"
a1= w[0]
a2=w[7]
a3=w[11]
acro= a1+a2+a3
print("Acronym of the given phrase Python for everyone:", acro)
print("Result of replace method:", w.replace('Everyone', 'All'))
print("Result of split method:", company.split(" "))
w="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("Result of split method:", w.split(","))
print("Character at index 0 of variable company:", company[0])
print("Character at last index of variable company:", company[-1])
print("Character at 10 index of variable company:", company[10])
