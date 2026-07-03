empty_tuple=()
spices=('Red Chilli', 'Pepper', 'Tumeric', 'Corriander')
print('Length of spices tuple: ', len(spices))
print('First index value of tuple: ', spices[0])
print('Middle index value of tuple: ', spices[len(spices)//2])
print('Last index value of tuple: ', spices[len(spices)-1])

middle= len(spices)//2
mid_item= spices[0:middle]
print("Start to middle elements of spices tuple: ", mid_item)

#Changing tuples to list
cartoons=('Tom & Jerry', 'Oggy & The cockroaches', 'Toy story', 'Scooby Doo')
tuple_list=list(cartoons) #Tuple to list
print("The data type of cartoons tuple is:", type(cartoons), "\n The datatype of list tuple_list:", type(tuple_list))

# List to tuple
meat_food=["Chicken", "Fish", "Beef", "Quail", "Veal", "Mutton"]
meats= tuple(meat_food)
print("Datatype of meat_food list:", type(meat_food), "Datatype of meat tuple:", type(meats))

#Checking an element exists in a tuple
print("Does chicken exists in tuple:",'Chicken' in meats)

#Joining Tuple
color1= ('yellow', 'orange', 'green')
color2=('blue', 'purple', 'indigo')
colors=color1+color2
print("Combining two tuples:", colors)

#Deleting tuple
del color1
#print("After deletinng colors tuple: ",color1) #Generates name error as tuple is deleted


