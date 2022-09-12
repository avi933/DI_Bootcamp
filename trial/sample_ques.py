import random
import json

class Question:
    questId = 0
    def __init__(self,question_text,correct_ans,bad_ans1,bad_ans2,bad_ans3) :
       self.questId = Question.questId
       self.question_text = question_text
       self.bad_ans1 = bad_ans1
       self.bad_ans2 = bad_ans2
       self.bad_ans3 = bad_ans3
       self.correct_ans = correct_ans
       Question.questId =+ 1 


# mylist = ["apple", "banana", "cherry","avishek","ramjeeawon"]
# random.shuffle(mylist)

# print(mylist)

x =  '{ "question":"what is html", "bad1":"hp", "bad2":"New", "bad3":"tension", "correct":"GOOD"}'
y = json.loads(x)
array_answer = [ y["bad1"],y["bad2"],y["bad3"],y["correct"]]
print(array_answer, "before shuffle")

shuffle = random.shuffle(array_answer)
print(array_answer," after shuffle" )
# print(y["question"])

