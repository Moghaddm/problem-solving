

class MyIterator:
    def __init__(self,max) -> None:
        self.current = 0
        self.max = max
    
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current + 1 > self.max: raise StopIteration
        self.current += 1
        return self.current

        
my = MyIterator(3)
my.__iter__()
print(my.__next__())
print(my.__next__())
print(my.__next__())
print(my.__next__())
