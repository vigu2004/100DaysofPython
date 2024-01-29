from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for i in range(len(question_data)):
    q = Question(text=question_data[i]["text"], answer=question_data[i]["answer"])
    question_bank.append(q)

q = QuizBrain(question_bank)

while q.still_has_question():
    q.next_question()

print("You've completed the quiz")
print(f"You got {q.score}/{len(question_bank)}!!")