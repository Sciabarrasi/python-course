empty_set = {} #thats not a set, its a dictionary
empty_set = set() #this is a set

numbers = {1,2,3,4,5} #this is a set
fruits = {"apple", "banana", "cherry"} #this is a set

#in a set we can´t have duplicates elements
for fruit in fruits:
    print(fruit)

print(numbers)
numbers.discard(3) #removes 3 from the set
print(numbers)

numbers.update([6,7,8]) #adds multiple elements to the set
print(numbers)

a = {1,2,3}
b = {4,5,6}

print(a | b) #union of two sets

print(a & b) #intersection of two sets

print(a - b) #difference of two sets

print(a ^ b) #symmetric difference of two sets

ids = {2,3,1,2,3,4,5} 

set(ids) #removes duplicates from the list
print(ids)