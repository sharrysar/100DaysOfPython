import html

class QuizBrain():
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, player_answer):
        correct_answer = self.current_question.answer
        if player_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

