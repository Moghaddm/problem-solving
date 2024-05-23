from computerAbstract import Computer
import time as t

class Teblet(Computer):
    def turnOn(self):
        t.sleep(1)
        self.isOn = True
        print(f"{self.name} is running now.")