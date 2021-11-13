from question_model import QuestionModel
from data import question_data, second_question_data
from quiz_brain import QuizBrain

question_bank = []

for value in second_question_data:
    question = value['question']
    answer = value['correct_answer']
    full_set = QuestionModel(question, answer)
    question_bank.append(full_set)

quiz = QuizBrain(question_bank)

while quiz.still_has_question() is not False:
    quiz.next_question()
    print("You have completed the quiz")
    print(f"Your final score was: {quiz.scores}/{len(question_bank)}")

