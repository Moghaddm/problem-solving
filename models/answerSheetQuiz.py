from quiz import Quiz

class AnswerSheetQuiz(Quiz):
    def __init__(self, title, time_limitation,rows) -> None:
        super().__init__(title, time_limitation)
        self.rows = rows
        
    def display(self):
        print("i cant show you main info about quiz. but these are rows: "+ ", ".join(self.rows))
            
    def __repr__(self) -> str:
        return f"this is {self.title} answer sheet quiz."