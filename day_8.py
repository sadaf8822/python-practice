empyth_dict={}
dct= {'key1': 'value1', 'key2': 'value2', 'key3':'value3'}
print("Length of dictionary:", len(dct))

#Accessing the dictionary items
print("Accessing the dictionary items using keys:", dct['key1'])
dct['key5']='value5'

person={ #Main dictionary
    'first_name':"Tom",
    'last_name':'Jerry',
    'age':'50',
    'country':'Norway',
    'is_married':True,
    'qualities':['mouse_catcher', 'adorable', 'mischief'], #List within dictionary
    'address': { #A dictionary within main dictionary
        'street': 'Bakers street',
        'zip_code': '2212'
    }
}
person['job_title']='Cat of the house' #Adding another key value pair
person['qualities'].append('clumsy') #Adding value to the list
print(person)

#Modifying the items of dictionary
person['first_name']='Thomas'
person['age']= '60'
print(person)

#Checking either a key exists within a dictionary
print("Does key2 exist within dictionary dct:",'key2' in dct)

#Popping a key
value_popped= dct.pop('key1')
#Popping a value
last_value_pop= dct.popitem()
print("Value popped:", value_popped, "\nLast value pop:", last_value_pop)
del dct['key2']

#Changes a dictionary into a list of tuples
car={'brand': 'Ford', 'model': 'mustang', 'year': 2024}
print(car.items())

#Clearing a dictionary
mlb_teams= {'Colorado': 'Rockies',
 'Minnesota': 'Twins', 
 'Seattle': 'Marriners', 
 'Milawakee': 'Brewers'
 }
print(mlb_teams.clear())

#Deleting a dictionary
del mlb_teams

#Copy dictionary
#Copy function can be used with list, dictionary, set. But not with tuple
places={'USA': 'New York', 'Afghanistan': 'Kabul', 'England': 'London', 'Phillipine': 'Manila'}
places_copy= places.copy()
print(places_copy)

#Combining two dictionaries together
num1={"a":1, "b":2}
num2={"c":3, "d":4}
print(num1|num2)
num1.update(num2) #Update function doesnot return
print(num1)

#Getting keys from a dictionary
water_bodies= {"Amazon_River": "South_America", "Onega_Lake": "Europe", "Ganges_River": "Asia", "Baikal_Lake": "Euro_Asia"}
keys=water_bodies.keys()
print(keys)

#Using values method to get values from a dictionary
values=water_bodies.values()
print(values)

#Using get method-- get method gets the values of the key given as argument
val= water_bodies.get("Amazon_River")
print("Amazon river is located in continent: ",val)