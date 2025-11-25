def greeting(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greeting("Alice", 30)

def fav_fruits(*fruits):
    print("Your favorite fruits are:")
    for fruit in fruits:
        print(f"- {fruit}")

fav_fruits("Apple", "Banana", "Cherry")

def user_profile(**info):
    print("User Profile:")
    for key, value in info.items():
        print(f"{key}: {value}")

user_profile_dict = {"name": "Bob", "age": 25, "city": "New York"}
user_profile(**user_profile_dict)