from answerSheetQuiz import *
from customQuiz import *
from laptop import *
from tablet import *

myList = ["first","second","third"]
iter = iter(myList)
print(iter)
print(next(iter))
print(next(iter))
print(next(iter))

print("this is another section. ------------------------")

customQuiz = CustomQuiz("c# course",120,["first question","second question"])
customQuiz.display()
customQuiz.start()
customQuiz.display()
print(customQuiz.__repr__())
print(f"this is time limitation of quiz: {customQuiz.time_limitation}")

answerSheetQuiz = AnswerSheetQuiz("python course",100,["first row","second row"])
answerSheetQuiz.display()
customQuiz.start()
answerSheetQuiz.display()
answerSheetQuiz.__title = 10

print("this is another section. ------------------------")

laptop = Laptop("mohammad laptop")
laptop.turnOn()

tablet = Teblet("mahdi tablet")
tablet.turnOn()

print("this is another section. ------------------------")







