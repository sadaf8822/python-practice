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


#Exercise-1
words=()
print("Showing an empty tuple:", words)
imaginary_sibling=('Sibling1', 'Sibling2')
brothers=('Sibling3',)
sisters=('Sibling4',)
sibling= imaginary_sibling +brothers+ sisters
print(sibling)
print('How many imaginary siblings do you have: ', sibling,len(sibling))

parent=('Mother', 'Father')
family_members=parent + sibling
print("Total family members are:", len(family_members))

parent1, parent2, *rest= family_members
print("Parents:", parent1, parent2)
print("Siblings:", rest)

siblings= family_members[-4:]
parents= family_members[0:2]
print(siblings)
print(parents)

fruits=('Orange', 'Banana', 'Mango', 'Apple', 'Grape', 'Apricot')
vegetables=('Onions', 'Potatoes', 'Tomatoes', 'Garlic', 'Ginger', 'Zucchini')
animal_products=('Milk', 'Eggs', 'Cheese', 'Leather')
food_stuff_tp= fruits + vegetables + animal_products
print(food_stuff_tp)
