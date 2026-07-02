empty_tuple=()
spices=('Red Chilli', 'Pepper', 'Tumeric', 'Corriander')
print('Length of spices tuple: ', len(spices))
print('First index value of tuple: ', spices[0])
print('Middle index value of tuple: ', spices[len(spices)//2])
print('Last index value of tuple: ', spices[len(spices)-1])

middle= len(spices)//2
mid_item= spices[0:middle]
print("Start to middle elements of spices tuple: ", mid_item)
