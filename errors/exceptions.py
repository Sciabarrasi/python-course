#exceptions is the same as errors
#try:
    #need to be an exception
#    result = 10 / 0
#except ZeroDivisionError:
#    print("Error: you cant divide by zero")

#try: 
    #logic that may cause different exceptions
#    number = int(input("Enter a number: "))
#except ValueError:
#    print("Error: Invalid input. Please enter a valid integer.")
#except KeyboardInterrupt:
#    print("\nProcess interrupted by user.")

try:
    file = open("existing_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    file.close()

try:
    print("Trying to execute some code...")
except ValueError:
    print("Caught a ValueError.")
else:
    print("No exceptions occurred.")

