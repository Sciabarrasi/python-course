#dictinary = key = value pair

empty_dict = {}

person = { "name": "Mark", "age": 30, "city": "New York"}

print(person['name']) #Mark
print(person.get('age')) #30

person['age'] = 31
print(person) # {'name': 'Mark', 'age': 31, 'city': 'New York'}

person['job'] = 'Engineer'
print(person) # {'name': 'Mark', 'age': 31, 'city': 'New York', 'job': 'Engineer'}


del person['city']
print(person) # {'name': 'Mark', 'age': 31, 'job': 'Engineer'}

person.pop('age')
print(person) # {'name': 'Mark', 'job': 'Engineer'}

elements = person.items()
print (elements)

for keys in person:
    print(keys) 


for keys in person.values():
    print(keys)

for keys, values in person.items():
    print(keys, values)