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

#Exercise-1
def add_two_nums(num1, num2):
    sum_two_nums= num1+num2
    return sum_two_nums
a= int(input("Enter a number:"))
b= int(input("Enter another number:"))
print("Sum of numbers entered is: ", add_two_nums(a,b))

def area_of_circle(r):
    pie= 3.14
    area_of_circle= pie* r * r
    return area_of_circle
radius=float(input("Enter your radius:"))
print("Area of circle: ", area_of_circle(radius))

def add_all_nums(*nums):
    total= 0
    for i in nums:
        total+=i
    return total
numbers= input("Enter some numbers but give space:")
nums_list= [int(n) for n in numbers.split()]
print("Total sum of numbers entered: ", add_all_nums(*nums_list))

def convert_celsius_to_fahrenheit(temp):
    f= temp * 1.8 +32
    return f
celsuis= float(input("Enter celsuis:"))
print("Fahrenheit Temperature:", convert_celsius_to_fahrenheit(celsuis))

def check_season(month):
    autumn= ['September','september' ,'October','october' ,'November', 'november']
    winter=['December','February','January','december','february','january']
    spring=['March', 'April', 'May', 'march', 'april', 'may']
    summer=['June', 'July', 'August','june', 'july', 'august']
    if month in autumn:
        print("The month {} is in autumn." .format(month))
    elif month in winter:
        print("The month {} is in winter." .format(month))
    elif month in spring:
        print("The month {} is in spring." .format(month))
    elif month in summer:
        print("The month {} is in summer" .format(month))
    else:
        print("Invalid entry")

month=str(input("Enter a month:"))
check_season(month)

def calculate_slope(m, b):
    print("y= {}x + {}" .format(m,b))
m=int(input("Enter the value of m: "))
b= int(input("Enter the value of b: "))
calculate_slope(m,b)

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "a cannot be zero"
        
    disc = b**2 - 4*a*c 
    
    if disc > 0:
        # Use / for true division instead of // (floor division)
        root1 = (-b + (disc**0.5)) / (2*a)
        root2 = (-b - (disc**0.5)) / (2*a)
        return root1, root2
    elif disc == 0:
        root = -b / (2*a)
        return root
    else:
        real_part = -b / (2*a)
        imaginary_part = (abs(disc)**0.5) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2
a= int(input("Enter a value for a: "))
b= int(input("Enter a value for b: "))
c= int(input("Enter a value for c: "))
print("Real distinct:", solve_quadratic_eqn(a,b,c))

# Case 2: One repeated root (x^2 - 4x + 4 = 0) -> Expected: (2.0,)
print("Repeated root:", solve_quadratic_eqn(a,b,c))

# Case 3: Complex roots (1x^2 + 1x + 1 = 0) -> Expected: (-0.5+0.866j, -0.5-0.866j)
print("Complex roots:", solve_quadratic_eqn(a,b,c))

num_list=int(input("Enter the length of list: "))
mango_list= []
for index in range(num_list):
    item= input(f"Enter element for index {index+1}:")
    mango_list.append(item)

def print_list(lst):
    for item in lst:
        print(item)

print_list(mango_list)

