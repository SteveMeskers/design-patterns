from abc import ABC
from collections.abc import Iterable


class Sumable(Iterable, ABC):
    @property
    def sum(self):
        total = 0
        
        for s in self:
            total += s if isinstance(s, int) else s.sum
            
        return total

class SingleValue(Sumable):
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        yield self.value
    

class ManyValues(list, Sumable):
    pass
            