import itertools

list = [1, 2, 3, 4, 5]

string = "Python"

print(string[::-1])

first, *rest = [1, 2, 3, 4, 5]
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]

matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

names = ["Alice", "Bob", "Charlie"]
ages = [23, 30, 35]

for names, ages in zip(names, ages):
    print(f"{names} is {ages} years old.")

over_ten = list(filter(lambda x: x > 10, [8, 11, 3, 24]))
print(over_ten)  # Output: [11, 24]

combined = list(itertools.chain([1, 2, 3], [4, 5, 6]))
print(combined)  # Output: [1, 2, 3, 4, 5, 6]

