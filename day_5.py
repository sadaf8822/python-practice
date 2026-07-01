code_lang=[]
code_lang=['html','css', 'js', 'reactjs']
print('List Code Language:', code_lang)
print('Length of list code language', len(code_lang))

#Accessing using positive index (Left index)
print("Element at 0 index: ", code_lang[0])
print("Element at 1 index:", code_lang[1])
print("Element at 2 index:", code_lang[2])
print("Element at 3 index:", code_lang[3])
#When to access from right (negative index)

#Assigning the first three indexes in variables and *rest catches the remaining items of list
first_element, second_element, third_element, *rest= code_lang
print(first_element)
print(second_element)
print(third_element)
print(rest)

#Slicing items
js_lang=code_lang[2:4]
print(js_lang)

#Modifying list
code_lang[0]='angular'
print(code_lang)

#Checking item in a list
does_exist= 'reactjs' in code_lang
print("Using operator with list:", does_exist)

#Adding items to list
new_lang= input("Which coding language are you using: ")
code_lang.append(new_lang)
print("Append function", code_lang)

#Insert items into a list (Insert Function)
code_lang.insert(2, "React Native")
print("Insert Function:",code_lang)

#Remove items into a list (remove function)
code_lang.remove("reactjs")
print("Remove function:", code_lang)

#Remove items into a list (pop function)
popped_index= code_lang.pop()
print(f"Result of popped variable {popped_index} \n Remaining list:", code_lang)

#Remove items into a list (del function)
del code_lang[0]
print(code_lang)

#Clear list items using clear builtin function
print("Before clearing list: ", code_lang)
code_lang.clear()
print("After clearing list: ", code_lang)

#Copying list
ai_frameworks=['keras, transformers, tensorflow']
code_lang_copy= ai_frameworks.copy()
print("Showing results of copy builtin function: ",code_lang_copy)

#Joining Lists
#Method-1: + operator
positive_integers=[1,2,3,4,5]
zero=[0]
negative_integers=[-5,-4,-3,-2,-1]
integers= negative_integers+ zero+ positive_integers
print("Joining lists using '+': ", integers)

#Method-2: extend method (builtin)
negative_integers.extend(zero)
negative_integers.extend(positive_integers)
print("Joining lists using extend method: ", negative_integers)

#Counting list items
redundant_list= ["tumeric", "pepper", "salt", "cajin", "tumeric", "chilli powder", "tumeric"]
print("Result of count method \n How many times did tumeric come in redundant list: ", redundant_list.count("tumeric"))

#Index method
#Shows the first occurrence, accesses for left to right
print("Finding index of tumeric:", redundant_list.index("tumeric"))

#Reverse list
redundant_list.reverse()
print("Reversing a list using reverse function: ", redundant_list)

#Sorting list items
#Method-1: Sort method
redundant_list.sort()
print("Result of sort method in ascending:", redundant_list)
redundant_list.sort(reverse=True)
print("Result of sort method in descending:", redundant_list)

#Sorted method-does not modify the original string
print("Result of sorted method in ascending:", sorted(redundant_list))
print("Result of sorted method in descending:", sorted(redundant_list,reverse=True))

#Exercise
#Level-1
empty_list=list() #List function, creates empty list

berries=['goose berry', 'strawberry', 'raspberry', 'mulberry', 'blueberries']
print("Length of berries list:", len(berries))

print("Getting the first element", berries[0])
middle_element=berries[len(berries)//2]
print("Getting the middle element:", middle_element)
last_element=berries[len(berries)-1]
print("Getting the last element:", last_element)

mixed_data_types=["Erika", 22, "Unmarried", {"address":"123 street block1"}]
print("Showing a mixed data type list:", mixed_data_types)

companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('Companies list:', companies)
print("Number of companies in list:", len(companies))
middle=companies[len(companies)//2]
print("First element of list:", companies[0])
print("Middle element of list:", middle)
print("Last element of list:", companies[len(companies)-1])

companies[0]='Deepseek'
print("Displaying modified list:", companies)

it_companies=[]
it_companies.insert(0, 'Intel')
print(it_companies)

print("Modified uppercase first element", companies[0].upper())
it_companies=' #'.join(companies)
print("Result of join function, joining a string with list:", it_companies)

exist= 'IBM' in companies
print("Is IBM apart of the list:", exist)

berries.sort()
print("Sorting the list using sort method", berries)

berries.reverse()
print("Reversed list", berries)

first_berry, second_berry, third_berry, *rest= berries
print(first_berry, second_berry, third_berry, rest)