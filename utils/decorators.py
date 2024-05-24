
def printForCalculations(func):
    def inner():
        print("this is before of function execution.")
        print(func())
        print("this is after of function execution.")
    return inner

def mul(func):
    def inner():
        x = func()
        return x * x
    return inner

def power(func):
    def inner():
        x = func()
        return x ** 2
    return inner

@printForCalculations
@power
@mul
def calculate(): return 10
    
print(calculate())
    
    