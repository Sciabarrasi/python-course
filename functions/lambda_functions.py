#lambda arguments: expression

operation = lambda a, b: a + b

print(operation(5, 6))  # Output: 11

number = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, number))
print(squared)  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

fruits = ['apple', 'banana', 'pineapple', 'cherry']
fruits_sorted = sorted(fruits, key=lambda x: len(x))
print(fruits_sorted)  # Output: ['apple', 'banana', 'cherry', 'pineapple']