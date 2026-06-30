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