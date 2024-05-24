
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

myIterString = iter("mohammad")
next(myIterString)
next(myIterString)
print(tuple(myIterString))

print("another section ------------------")
first = [1,2,3,4]
second = [2,3,4,5,6]

dictio = dict(zip(first,second))
result= {key * 2 :value for key,value in dictio.items()}
print(result)


