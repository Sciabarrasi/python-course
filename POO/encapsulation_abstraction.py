from abc import ABC, abstractmethod

class stats_calc(ABC):
    def __init__(self, data):
        self.data = data
    
    @abstractmethod
    def calculate(self):
        pass

#need to create another class that inherits from stats_calc, because stats_calc is abstract
class calcMedia(stats_calc):
    def calculate(self):
        return sum(self.data) / len(self.data)
    
class calcVariation():
    def __init__(self, data):
        self.data = data
        self.calculator_media = calcMedia(data)

    def calculateVariant(self):
        media = self.calculator_media.calculate()
        return sum((x - media) ** 2 for x in self.data) / len(self.data)


data = calcVariation([3,6,8])



# Encapsulation and Abstraction Example
#class DataSet:

#    def __init__(self, data):
#        self._data = data  # Private attribute
#        self._height = len(data)

#    def media(self):
#        return sum(self._data) / self._height
    
#    def variation(self):
#        mu = self.media()
#        return sum((x - mu) ** 2 for x in self._data) / self._height
    
#    def get_data(self):
#        return self._data.copy()  # Return a copy to prevent external modification

# Example usage
#data = DataSet([4, 3, 7])
#print(data.get_data())  # [4, 3, 7]
