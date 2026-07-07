count=0
while count<5:
    print(count)
    count+=1

while count<5:
    print(count)
    count+=1
else:
    print("Printing else block",count)

num=0
while num<5:
    print(num)
    num+=1
    if num==3:
        print("Printing if block")
        break  #breaks a loop

val=0
while val <5:
    if val == 3:
        val +=1
        continue  #Continue keyword skips the current iteration and 
        #continues with the next, here 3 will be skipped
    print("Printing after continue keyword",val)
    val+=1

numbers_lt=[0,1,2,3,4] #List and for loop
for number in numbers_lt:
    print("Printing the list:",number)

berries_tpl=("Raspberry", "Mulberry", "Blackberry")
for berries in berries_tpl: #Tuple and for loop
    print("The elements in tuple are:", berries)

person= {
    'first_name': 'John',
    'last_name' : 'Doe',
    'age' : '32',
    'country' : 'France',
    'is_married': True,
    'skills':['Javascript', 'React', 'Nodejs', 'MongoDB', 'Python'],
    'address':{
        'street': 'Bakers street',
        'zipcode':'09092'
    }
}
for key in person:
    print("Keys in dictionary:",key)
for key,value in person.items():
    print("Keys and values of dictionary:",key, value)

companies_st= {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in companies_st:
    print("Companies set:", company)

even_num=(0,2,4,6,8)
for num in even_num:
    print(num)
    if num==3:
        break

#range(start, end, step)
lst=list(range(11)) #Here by default start=0, increment=1, where end=11
print(lst) #It will display 0-10 elements, making 11 elements

st=set(range(1,11)) #Here we gave the starting point=1, ending=11
print(lst)

lst=list(range(0,11,2)) #Start=0, end=11, skip/step=2
print(lst)
st=set(range(0,11,2))
print(st)

lst=list(range(11,0,-2)) #Here we have given for backward, start=11, end=0, skip=-2
print(lst)

#Nested loop
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# For else
for number in range(11):
    print(number)
else:
    print("The loop stops at:", number)

for number in range(6):
    pass 

counter=0
while counter<11:
    print("Iterating from 0 to 10:", counter)
    counter+=1

negative_counter= 10
while negative_counter>0 or negative_counter==10:
    print("Going backward using while loop:", negative_counter)
    negative_counter-=1

#for i in range(1, 8):
    #print("#" * i)

for i in range(8): #Row
    for j in range(8): #Column
        print(" # ", end="")
    print()    

for i in range(11):
    print("{} x {}= {}" .format(i, i, i*i))

py_lt=["Python", "Numpy", "Pandas", "Django","Flask"]
for element in py_lt:
    print("Elements of py_lt:", element)

for number in range(0, 101,2):
    print("Even number:", number)
