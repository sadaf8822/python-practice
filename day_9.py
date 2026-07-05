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