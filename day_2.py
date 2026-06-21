# Variables, Builtin Functions, Datatypes, Casting
#Builtin Functions
#Exercise-1
print('Hello World') #Displays output
len('Hello World') #Tells about length
type('Hello , World') #Displays data type
str(10) #converts a number to string
int('10') #converts into integer
float(10) #converts into float
input('Enter your name: ') #asks for input 
#help('keywords') #prints necessary keywords

#Exercise-2
print(min(20, 30, 40, 50)) #gives minimum value
print(max(20, 30, 40, 50)) #gives maximum value
min([20, 30, 40, 50]) #takes a list as an argument and returns min value
max([20, 30, 40, 50]) #takes a list as an argument and returns max value
print(sum([20, 30, 40, 50])) #takes a list as an argument and returns the sum

#Variables
first_name='Python'
last_name='Language'
country='python island'
city='snakes'
is_married= True
skills= ['venom', 'attack'] #list

person_info= { #dictionary
    'first_name': 'person1',
    'last_name' : 'someone',
    'country' : 'Fin',
    'city' : 'ending'
}
print(type(person_info))
print(type(skills))

# Checking Data Types
print(type('Python')) #str
print(type(first_name)) #str
print(type(10)) #int
print(type(2.11)) #float
print(type(1 + 1j)) #complex
print(type(True)) #bool
print(type([1,2,3,3])) #list
print(type({'name' : 'cece'})) #dictionary
print(type((1,2))) #tuple
print(type(zip([1,2], [3,4]))) #zip

#Casting
#int to float
num_int= 10
print('num_int', num_int)
num_float = float(num_int)
print('num_float:', num_float)

#float to int
gravity=9.81
print(int(gravity))

#int to str
num_int=10
print(num_int)
num_str=str(num_int)
print(num_str)

#str to int or float
num_str= '10.6'
num_float= float(num_str) #conversion of string to float
num_int= int(num_float) #conversion of float to int
print('num_int', int(float(num_str))) #conversion of string to int
print('num_float', float(num_str))
num_int= int(num_float)
print('num_int', int(num_int))

#str to list
first_name= 'python'
print(first_name)
first_name_tolist=list(first_name) #conversion of variable into list
print(first_name_tolist)

#Exercise-1
fname, lname, full_name, country, city, age, ismarried, is_true, is_light_on= 'Jane', 'Doe', 'Jane Doe Like', 'NA', 'NA', '99', 'Married', 'True', 'On'
print(type(fname))
print(type(lname))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(ismarried))
print(type(is_true))
print(type(is_light_on))
var1= len(fname)
var2= len(lname)
print('Length of first name:', var1)
print('Length of last name:', var2)
print('Maximum length of variable', max(var1, var2))

#Exercise-2
num_one=5
num_two=4
total=num_one+ num_two
diff= num_one - num_two
product= num_one* num_two
division= num_one / num_two
remainder= num_one%num_two
exp=num_one ** num_two
floor_division= num_one // num_two

radius=30
area_of_circle= 3.14 * radius
print("Area of circle:", area_of_circle)
rad2= float(input("Enter radius"))
circum_of_circle= 2* 3.14 *rad2
print("circumference of circle:", circum_of_circle)

first= input("Enter first name:")
last= input("Enter last name:")
country1= input("Enter country name:")
age1= input("Enter age of person:")
print(first, last, country1, age1)