import random

from data import question_data


class Question:
    def __init__(self, q_question, q_answer):
        self.question = q_question
        self.answer = q_answer


class QuizBrain:
    def __init__(self, q_question_list):
        self.number = 0
        self.score = 0
        self.question_list = q_question_list

    def new_question(self):
        current_question = self.question_list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}:{current_question.question} (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if self.number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"It's right!\nAnswer : {correct_answer}\nYour score {self.score}/{self.number} ")
        else:
            print(f"It's not right!\nAnswer : {correct_answer}\nYour score {self.score}/{self.number} ")
        print(" ")


question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.new_question()

print("You've completed the quiz")
print(f"Your final score : {quiz.score}/{quiz.number}")
