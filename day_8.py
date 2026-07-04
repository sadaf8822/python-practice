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

