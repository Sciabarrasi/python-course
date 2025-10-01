#dictionaries
my_dict = {"value1": 10, "value2": 20, "value3": 30}

my_dict["value2"] = 25  # Modifying an existing value
my_dict["value4"] = 40  # Adding a new key-value pair
my_dict.pop("value3")  # Removing a key-value pair
print(my_dict)

for key, value in my_dict.items():
    print(f"key: {key}: , value: {value}")

for element in my_dict:
    print(f"key: {element}, value: {my_dict[element]}")

print(my_dict.keys())
print(my_dict.values())

#sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}

set3 = set1 | set2  # Union
print(set3)
len(set3)

List = {1,3,3,5,7,7,}

set(List)
print(List)
print(len(List))