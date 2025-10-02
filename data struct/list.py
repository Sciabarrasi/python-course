L1 = [2,3,4]

print(L1)

fruits = ['apple', 'banana', 'cherry']
print(fruits[1])  # Output: banana

fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, 'kiwi')
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']

fruits.remove('banana')
print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange']

del fruits[0]
print(fruits)  # Output: ['kiwi', 'cherry', 'orange']

last = fruits.pop()
print(last)  # Output: orange

for fruit in fruits:
    print(fruit)

word = "HELLO"
letters = list(word)
print(letters)  # Output: ['H', 'E', 'L', 'L', 'O']