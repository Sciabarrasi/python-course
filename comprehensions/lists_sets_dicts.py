#new expression with for and if
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]

#new expression with for in iterable if condition
squares_set = {x**2 for x in range(10)}
print(squares_set)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

#new key: value for key, value in iterable if condition
squares_dict = {x: x**2 for x in range(1,5)}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16}
