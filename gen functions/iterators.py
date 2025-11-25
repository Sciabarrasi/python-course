#iterator example
class Counter:
    def __init__(self, low, high):
        self.actual = low
        self.high = high

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.actual < self.high:
            number = self.actual
            self.actual += 1
            return number
        raise StopIteration
    
#using the iterator
#for num in Counter(3, 8):
#    print(num)

#generator example with yield
def counter(low, high):
    while low < high:
        yield low
        low += 1

for i in counter(3, 8):
    print(i)

