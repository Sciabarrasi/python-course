#functions that return multiple values

def basic_operations(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    if b != 0:
        quot_result = a / b
    return print(sum_result, diff_result, prod_result, quot_result if b != 0 else None)

# Example usage:
basic_operations(16,4) # the result is a tuple with 4 values

sum_result, diff_result, prod_result = basic_operations(16, 4) # unpacking the returned tuple into separate variables

print("Sum:", sum_result)
print("Difference:", diff_result)