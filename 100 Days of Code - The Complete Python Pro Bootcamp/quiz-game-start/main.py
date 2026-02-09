from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_item = Question(item['text'], item['answer'])
    question_bank.append(question_item)

quiz = QuizBrain(question_data)

while quiz.still_has_questions:
    quiz.next_question()