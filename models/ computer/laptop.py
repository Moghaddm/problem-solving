from computerAbstract import Computer
import time as t

class Laptop(Computer):
   def turnOn(self):
       t.sleep(5)
       self.isOn = True             
       print(f"{self.name} is running now.")