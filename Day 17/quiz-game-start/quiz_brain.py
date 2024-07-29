class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        """This function checks if there are still questions to ask the user based on which returns True/False."""
        length = len(self.question_list)
        if self.question_number >= length:
            return False
        return True

    def check_answers(self, user_answer, correct_ans):
        """This function checks the user answer and prints the score."""
        if user_answer.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong :(")
        print(f"The correct answer is {correct_ans}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")

    def next_question(self):
        """This function asks questions to the user and calls the check_answers function"""
        current_question = self.question_list[self.question_number]
        correct_answer = self.question_list[self.question_number]
        right_ans = correct_answer.correct_ans
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False)?: ")
        self.check_answers(user_answer, right_ans)
        return self.question_number


