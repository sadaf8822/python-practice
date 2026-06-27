#Operators
age= 30
height=5.5
complex_num= 12 + 1j
#Area of triangle
base= float(input("Enter base:"))
height1= float(input("Enter height:"))
area_of_triangle= 0.5* base * height1
print("Area of triangle:", area_of_triangle)

#Perimeter of triangle
side1= float(input("Enter side1:"))
side2= float(input("Enter side2:"))
side3= float(input("Enter side3:"))
print("Perimeter of triangle:", side1+side2+side3)

# Area of Circle
pi=3.14
radius= float(input("Enter the circle's radius:"))
area_of_circle=pi*radius**2

# Circumference of circle
circum= 2*pi*radius
print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum)

# X-intercept and Y-intercept of slope y=2x-2
#slope formula y=mx+b
m=2
#y intercept is when x=0 so b is y intercept
b=-2
#x intercept is when y=0
# 0= mx+b -> -b= mx -> x= -b/m
# x= -(-2)/2 => 1
x=1
print("Value of slope:", m)
print("Value of y intercept", b)
print("Value of x intercept", x)

# Slope and Euclidean distance
#Formula of slope= m= y2-y1/x2-x1
#Euclidean Distance= d= sq_root[(x2-x1)^2 + (y2-y1)^2]
# points x(2,2), y(6,10)
x1, x2, y1, y2= 2,2,6,10
print("x2-x1=", x2-x1)
print("y2-y1", y2-y1)
Euclidean_distance= ((x2-x1)**2+(y2-y1)**2)**0.5
print("Euclidean Distance:", Euclidean_distance)

m1= 0
print(m>m1)
print(m<m1)
print(m==m1)

# Find value of y for equation y=x^2+ 6x+ 9
# Put different values of x
x= int(input("Enter the value of x:"))
y= x**2 + 6*x + 9
print("Value of y:", y)
print("When value of x is:", x)

# To find the value of x when y=0
a,b,c=1,6,9
disc= (b**2) - (4*a*c)
x_unknown= (-b + (disc**0.5)) / (2*a)
print("Value of x:", x_unknown)

# Find and show false msg when comparing words given
print(len('python') != len('dragon'))

#Comparison operator usage: in, and
print('on' in 'python' and 'on' in 'dragon')

#Comparison operator usage: in operator
print("Is usage of word jargon found: ",'I hope this course is not full of jargon' in 'jargon')

print("There is no usage of letters 'on' in python and dragon", 'on' not in 'python' and 'no' not in 'dragon')

text=len('python')
text_converted= str(float(text))
print('Text datatype is: ', type(text_converted))

#Even or odd
num=int(input("Enter a number to check even or odd:"))
result= num % 2
print("The number is odd or even: ", result)

#Floor division and casting
n=7//3
print("Result of floor division 7//3:", n)

print(type('10')== type(10))
val=int(9.8)
print(val == 10)
#Calculate weekly earnings
hr=int(input("Enter work hours: "))
rate_per_hr= int(input("Enter rate per hours: "))
weekly_earning= hr * rate_per_hr
print("Your weekly earnings are:", weekly_earning)
#Calculate number of years in seconds
yrs=int(input("Enter the number of years you have lived: "))
yrs_in_sec= yrs * 365.25 * 24 * 60 * 60
print("Years in seconds is:", yrs_in_sec)

print(1**1, 1**2, 1**3, 1**4, 1**5)
print(2**1, 2**2, 2**3, 2**4, 2**5)
print(3**1, 3**2, 3**3, 3**4, 3**5)
print(4**1, 4**2, 4**3, 4**4, 4**5)
print(5**1, 5**2, 5**3, 5**4, 5**5)