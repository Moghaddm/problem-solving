
class Quiz:
    
    # constructor
    
    def __init__(self,title,time_limitation) -> None:
        self.__title = title
        self.__time_limitation= time_limitation
        self.is_running = False
    
    # properties
            
    def get_title(self): return self.__title
    
    def set_title(self,title):
        if len(title) < 3: raise ValueError("title of quiz cannot be less than 3 characters.")
        self.title = title 

    @property
    def time_limitation(self):
        return self.__time_limitation
    
    @time_limitation.setter
    def time_limitation(self,time_limitation):
        self.__time_limitation = time_limitation
    
    # methods and behaviors
    
    def start(self):
        self.is_running = True
        
    def finish(self):
        self.is_running = False
        
    def display(self):
        print(f"{self.__title} is {'running' if self.is_running else 'not running'} right now",end=" ")
        
    def __len__(self):
        return self.__time_limitation