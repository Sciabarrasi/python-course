class DataSet:
    data = "numeric"
    def __init__(self, data):
        self.data = data

    def media(self):
        return sum(self.data) / len(self.data)
    
    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        midpoint = n // 2
        if n % 2 == 0:
            return (sorted_data[midpoint -1] + sorted_data[midpoint]) / 2
        else:
            return sorted_data[midpoint]
        
    def add_data(self, new_data):
        self.data.append(new_data)
        
my_data = DataSet([1, 2, 3, 4, 5, 10, 8])
print(my_data.media())

print(my_data.data)
my_data.add_data(20)
print(my_data.data)