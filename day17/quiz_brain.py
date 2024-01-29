class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, x):
        if answer == x:
            print("You are correct")
            self.score += 1
        else:
            print("You are incorrect")
        print(f"The correct answer was {answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        x = input(f"Q.{self.question_number} {current_question.text} (True/False)")
        self.check_answer(current_question.answer, x)
