#lists and tuples

my_list = [1, 2, 3, "Hello", True]
my_tuple = (1, 2, 3, "Hello", True)

print(my_list[0]) # Accessing list element
print(my_tuple[1]) # Accessing tuple element

my_list[2] = "Changed" # Modifying list element
print(my_list)

#my_tuple[2] = "Changed" # This will raise an error since tuples are immutable
#print(my_tuple)

my_list.append("New Element") # Adding element to list
print(my_list)

len(my_tuple) # Getting length of tuple
print(len(my_tuple))

my_tuple[2:4] # Slicing tuple
print(my_tuple[2:4])

my_list.remove(2) # Removing element from list
print(my_list)

L1 = ["a", "b", "c"]
L2 = L1

print(L2)
L2[1] = "Z"