class DataSet:

    def __init__(self, data):
        self.data = data
        self.size = len(data)

    def media(self):
        return sum(self.data) / len(self.data)
    
    def __str__(self):
        return f"DataSet(data={self.data}, size={self.size}, media={self.media():.2f})"
    
class DataSetPlus(DataSet):
    def desv_standart(self):
        mu = self.media()
        return (sum((x - mu) ** 2 for x in self.data) / self.size) ** 0.5
    
    def __str__(self):
        return f"DataSetPlus(data={self.data}, size={self.size}, media={self.media():.2f}, desv_std={self.desv_standart():.2f})"
    
big_data = DataSet([13,5,8])
big_data.media()
big_data_plus = DataSetPlus([13,5,8])
print(big_data)
big_data_plus.media()
print(big_data_plus)

