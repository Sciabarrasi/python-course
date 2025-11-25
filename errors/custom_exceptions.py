class MyError(Exception):
    #class based on Exception
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def verify_value(value):
    if value < 0:
        raise MyError("Value cannot be negative")
    else:
        print("Value is valid:", value)

try:
    verify_value(-10)
except MyError as e:
    print("Caught an error:", e)