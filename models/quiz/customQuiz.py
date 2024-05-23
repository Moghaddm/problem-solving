from quiz import Quiz

class CustomQuiz(Quiz):
    
    # constructor
    
    def __init__(self, title, time_limitation,questions) -> None:
        super().__init__(title, time_limitation)
        self._questions = questions
    
    @property
    def questions(self): return self._questions
    
    @questions.setter
    def questions(self,questions): self.questions = questions
    
    # methods and behaviors
        
    def display(self):
        super().display()
        print("and these are questions of that: {}".format(", ".join(self._questions)))
        
    def __repr__(self) -> str:
        return f"this is {self.get_title()} custom quiz."
    
    
    
customQuiz = CustomQuiz("c# course",120,["first question","second question"])
customQuiz.display()
customQuiz.start()
customQuiz.display()
print(customQuiz.__repr__())
print(f"this is time limitation of quiz: {len(customQuiz)}")