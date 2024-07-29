from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# to format the questions and answers into lists making the qns and ans as attributes
for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

# creating the class QuizBrain
quiz_brain = QuizBrain(question_bank)

# Asking the user all questions until the last question in the list
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")