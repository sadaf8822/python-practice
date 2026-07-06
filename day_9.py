a=3
if a>0:
    print("A is a positive number")

b=9
if b<0:
    print("B is a negative number")
else:
    print("B is a positive number")

num=0
if num>0:
    print("num is a positive number")
elif num<0:
    print("Num is a negative number")
else:
    print("num is zero")

#Multiple conditions with and operator
if a>0 and a%2==0:
    print("A is an even number and a positive")
elif a>0 and a%2 !=0:
        print("A is a positive number")
elif a==0:
    print('A is zero')
else:
    print("A is a negative number")

if a>0: #Nested
    if a%2==0:
        print("A is a positve and even integer")
    else:
        print("A is a positive number")
elif a==0:
    print("A is zero")
else:
    print("A is negative number")

user="Rome"
access_level=4
if user == 'admin' or access_level >=4:
    print("Welcome user:", user)
else:
    print("Access Not granted")

#Exercise Level1
age= int(input("Enter your age:"))
remaining_yrs= 18-age
if age>=18:
    print("You are old enough to drive")
else:
    print("You need {} more years to learn to drive" .format(remaining_yrs))

my_age= int(input("Enter my age:"))
your_age= int(input("Enter your age:"))
difference_myage= my_age - your_age
difference_yourage= your_age - my_age

if my_age>your_age:
    print("I am {} years older than you" .format(difference_myage))
elif my_age == your_age:
    print("We are of the same age")
else:
    print("You are {} years older than me" .format(difference_yourage))

grade=int(input("Enter your marks: "))
if grade==100 or grade >= 90:
    print("90-100 grade: A")
elif grade==89 or grade >= 80:
    print("80-89 grade: B")
elif grade==79 or grade >= 70:
    print("70-79 grade: C")
elif grade==69 or grade >= 60:
    print("60-69 grade: D")
elif grade==59 or grade >= 0:
    print("0-59 grade: F")
else:
    print("Invalid marks entered") 

month=str(input("Enter a month:"))
autumn= ['September','september' ,'October','october' ,'November', 'november']
winter=['December','February','January','december','february','january']
spring=['March', 'April', 'May', 'march', 'april', 'may']
summer=['June', 'July', 'August','june', 'july', 'august']

if month in autumn:
    print("It is autumn in {}" .format(month))
elif month in winter:
    print("It is winter in {}" .format(month))
elif month in spring:
    print("It is spring in {}" .format(month))
elif month in summer:
    print("It is summer in {}" .format(month))
else:
    print("Invalid entry")

num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
if num1> num2:
    print("{} is greater than {}".format(num1,num2))
elif num2> num1:
    print("{} is greater than {}".format(num2,num1))
else:
    print("{} is equal to {}".format(num1, num2))

fruits = ['banana', 'orange', 'mango', 'lemon']
user_input=str(input("Enter your favorite fruit:"))

if user_input not in fruits:
    fruits.append(user_input)
    print("Modified list of fruits:", fruits)
else:
    print("This fruit exists")

person={
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 50,
    'country': 'Ireland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
person_skillset=person['skills']
if person['skills']== person_skillset:
    print("It exists!!")
    mid= len(person)//2
    mid_skill= person_skillset[mid]
    print("The middle skillset is:", mid_skill)

if 'Python' in person['skills']:
    print("The person has Python skills")
if 'Javascript' in person['skills'] or 'React' in person['skills']:
     print("This is a frontend developer")
if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print("This is a backend developer")
if 'React'in person['skills'] and 'Node'in person['skills'] and 'MongoDB' in person['skills']:
    print("This is a fullstack developer")
if person['is_married'] is True and person['country']== 'Ireland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")