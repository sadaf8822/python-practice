#Function without parameters
def generate_full_name():
    first_name= 'Ibrahim'
    last_name= 'Isa'
    space= ' '
    full_name= first_name + space + last_name
    print(full_name)
generate_full_name()

#Function that returns a value
def add_two_number():
    num_one=2
    num_two=3
    total= num_one + num_two
    return total

print(add_two_number())

#Function that takes one argument
def sum_of_numbers(n): #10
    total_sum=0
    for i in range(n+1): #10+1
        total_sum+=i #55
    return total_sum
print(sum_of_numbers(10))

# Function with two arguments
def calculate_age(current_yr, birth_yr):
    age= current_yr - birth_yr
    return age
print("Age:", calculate_age(2021, 1993))

# Passing arguments with key and value
def area_triangle(length, width):
    area_triange= length * width
    return area_triange
print("Area of triangle:",area_triangle(width= 45, length=23))

#Returning list
def find_even_numbers(n):
    even = []
    for i in range(n+1):
        if i%2 == 0:
            even.append(i)
    return even
print(find_even_numbers(10))

#Function with default parameters
def greetings(name= 'Peter'):
    message= name + ', welcome to Python'
    return message
print(greetings()) #Here using default parameter
print(greetings('Asif')) #If another value is not given, default value is used

#Taking arbitrary number of arguments
def sum_all_nums(*nums):
    total=0
    for num in nums:
        total +=num
    return total
print(sum_all_nums(2,3,4))

#Default and arbitrary number of parameters
def generate_groups(team='player1', *args):
    print(team)
    for i in args:
        print(i)
generate_groups('Asad', 'Ali', 'Amir')

# Dictionary Unpacking
def greet(name, location):
    print("Hi", name, "how is the weather in", location)
dictionary= {"name": 'Alice', "location": "Wonderland"}
greet(**dictionary)

#Function as a parameter of another function
def sq_num (n):
    return n**n
def do_something(f,x):
    return f(x)
print(do_something(sq_num, 3))