from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for items in question_data :
    question = items["text"]
    answer = items["answer"]
    questions = Question(question, answer)
    question_bank.append(questions)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("you completed the quiz.")
print (f"your final score is : {quiz.score}/{quiz.question_number} ")
