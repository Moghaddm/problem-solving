
class Quiz:
    def __init__(self,title,time_limitation) -> None:
        self.title = title
        self.time_Limitation= time_limitation
        self.is_Running = False
    
    _d=1
    
    def start(self):
        self.is_Running = True
        
    def finish(self):
        self.is_Running = False
        
    def display(self):
        print_quiz_running_state(self.title,self.is_Running)
        
class CustomQuiz(Quiz):
    def __init__(self, title, time_limitation,questions) -> None:
        super().__init__(title, time_limitation)
        self.questions = questions
        self.__private = "w"
        
    def display(self):
        super().display()
        print("and these are questions of that: "+", ".join(self.questions))
        
class AnswerSheetQuiz(Quiz):
    def __init__(self, title, time_limitation,rows) -> None:
        super().__init__(title, time_limitation)
        self.rows = rows
        
    def display(self):
        print("i cant show you main info about quiz. but these are rows: "+ ", ".join(self.rows))

def print_quiz_running_state(title,is_running):
    print(f"{title} is {'running' if is_running else 'not running'} right now",end=" ")

# procedural section

customQuiz = CustomQuiz("c# course",120,["first question","second question"])
customQuiz.display()
customQuiz.start()
customQuiz.display()

answerSheetQuiz = AnswerSheetQuiz("python course",100,["first row","second row"])
answerSheetQuiz.display()
customQuiz.start()
answerSheetQuiz.display()




