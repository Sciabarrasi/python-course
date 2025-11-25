if True: #with the : because it's a code block, if we dont have :, throw an error
    print("This is a type error" + 5)  # TypeError: can only concatenate str (not "int") to str

greetings = "Hello" # So I declared greetings variable
print(greetings) #theres not existing greetings variable, so NameError: name 'greetings' is not defined
#now the print, runs well

print('3'+'6') #return a '36' string, because both are strings
print(int('3') + int('6')) #return a 9 integer, because both are converted to integers

my_list = [1, 2, 3]
print(my_list[4])  # IndexError: list index out of range

my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])  # KeyError: 'c'

a = '99' 
int(a)  # This works fine, but if a was 'abc', it would raise a ValueError

'hello'.push('world') # AttributeError: 'str' object has no attribute 'push'


