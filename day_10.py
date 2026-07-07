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

