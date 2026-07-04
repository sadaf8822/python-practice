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

#Intersection
fruits={'Apricot', 'Apple', 'Mango', 'Banana'}
fruits2={'Apricot', 'Apple'}
common_fruits= fruits.intersection(fruits2)
print("Result of intersection between two sets: ",common_fruits)

#Superset and subset
print("Is fruits a superset:", fruits.issuperset(fruits2)) #operator (fruits >= fruits2)
print("Is fruits2 a subset:", fruits2.issubset(fruits)) #operator (fruits2 <= fruits)

#Difference between two sets
#Method-1
st1={1,2,3,4}
st2={5,6,7,8}
print(st2-st1)
#Method-2
a={1,2,3,10,100}
b={10,20}
c={100, 200}
print(a.difference(b,c)) #a-b= result, result-c

#Symmetric Difference, finds unique elements across given sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}
print(set1 ^ set2)
print(set1 ^ set2 ^ set3)

#Disjoint, having no common values
print(set1.isdisjoint(set2))

#Exercise
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print('Length of set it companies: ', len(it_companies))
it_companies.add("Twitter")
new_companies= {'Intel', 'Spacex', 'Notion', 'OpenAI'}
it_companies.update(new_companies)
print("New elements updated in the set:", it_companies)
it_companies.remove("Twitter")

#Difference between remove and discard function is
#discard function gives no error while the other gives keyerror msg

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print("Combining set A and B: ", A.union(B))
print("Intersection between set A and B: ", A.intersection(B))
print("Is A set a subset of set B:", A.issubset(B))
print('Are set A and set B disjoint (no common element): ', A.isdisjoint(B))
print("Joining set A with set B:", A|B)
print("Joining set B with set A: ", B|A)
print("The symmetric difference between set A and set B: ", A.symmetric_difference(B))
del A 
del B 

age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set= set(age)
print("Datatype of age list:", type(age), "Datatype of age_set:", type(age_set))
