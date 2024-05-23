from abc import ABC,abstractmethod

class Computer(ABC):
    def __init__(self,name) -> None:
        self.isOn = False
        self.name = name
    
    @abstractmethod
    def turnOn(self):
        pass