class QuizBrain():
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.still_has_questions = self.question_number < len(self.questions_list)
        self.score = 0

    # def still_has_questions(self):
    #     return self.question_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.question_number]
        sn = self.question_number + 1
        user_answer = input(f'Q.{sn}. {question['text']} (True/False)? ').title()

        self.check_answer(user_answer, question['answer'])
        self.question_number += 1

        self.show_result()

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You are right!')
            self.score += 1
        else:
            self.still_has_questions = False
            print('Oops, you got it wrong.')
            print(f'Correct answer was: {correct_answer}')
        print(f'Your score: {self.score}/{len(self.questions_list)} \n')

    def show_result(self):
        if not self.still_has_questions:
            print(f'Your final score is {self.score}/{len(self.questions_list)}')

