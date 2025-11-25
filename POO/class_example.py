class DataSet:
    type_data = "numeric"

    def __init__(self, type_data):
        self.data = type_data

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