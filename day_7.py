st={*()} #Empty set
#Checking datatype
print("Datatype of st:", type(st))

berries={'goose berry', 'strawberry', 'raspberry', 'cranberry', 'blueberry'}
#Length of set
print("Number of berries within set berries: ", len(berries))
#Does an element exist within a set
print("Does blueberry exist within berries set: ", 'blueberry' in berries)

#Taking one input
new_berry=input("Enter a new berry:")
berries.add(new_berry)
print(berries)

#Taking multiple inputs
new_berry1, new_berry2, new_berry3=input("Enter two to three berries:").split()
berries.update([new_berry1, new_berry2, new_berry3])
print(berries)

berries.remove('raspberry')
removed_berry=berries.pop()
print(removed_berry)

#berries.clear()
#print(berries)

del st

#Converting list to set
vegetables=['zucchini','onion', 'radish', 'eggplant', 'lady finger', 'bitter gourd']
veg_set= set(vegetables)
print("Datatype of vegetables list: ", type(vegetables), '\nDatatype of veg_set: ', type(veg_set))

#Converting a set to list
integers={1,2,3,4}
integers_lt= list(integers)
print("Datatype of integers set: ", type(integers), '\nDatatype of integers_lt: ', type(integers_lt))

#Joining sets
positive_integers={1,2,3,4}
zero={0}
negative_integers={-1,-2,-3,-4}
integers=positive_integers| zero #Joining
print(integers)
print(integers.union(negative_integers)) #Joining
