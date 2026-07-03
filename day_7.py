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

