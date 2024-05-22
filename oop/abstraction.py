from abc import ABC,abstractmethod
import time as t

class Computer(ABC):
    def __init__(self,name) -> None:
        self.isOn = False
        self.name = name
    
    @abstractmethod
    def turnOn(self):
        pass
         
class Laptop(Computer):
   def turnOn(self):
       t.sleep(5)
       self.isOn = True             
       print(f"{self.name} is running now.")

class Teblet(Computer):
    def turnOn(self):
        t.sleep(1)
        self.isOn = True
        print(f"{self.name} is running now.")