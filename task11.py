class Question:
    def __init__(self, question, options, correct_answer):
        self._question = question
        self._options = options
        self._correct_answer = correct_answer

    def get_question(self):
        return self._question

    def get_options(self):
        return self._options

    def get_correct_answer(self):
        return self._correct_answer

    def set_question(self, question):
        self._question = question

    def set_options(self, options):
        self._options = options

    def set_correct_answer(self, correct_answer):
        self._correct_answer = correct_answer


def play_quiz(questions, players):
    player_scores = [0] * len(players)

    for i, player in enumerate(players):
        print(f"\nИгрок {player}, ваша очередь!\n")

        for j, question in enumerate(questions):
            print(f"Вопрос {j + 1}: {question.get_question()}")
            for k, option in enumerate(question.get_options(), start=1):
                print(f"{k}. {option}")

            answer = int(input("Выберите номер правильного ответа: "))

            if answer == question.get_correct_answer():
                player_scores[i] += 1
                print("Верно!\n")
            else:
                print(f"Неверно. Правильный ответ: {question.get_correct_answer()}\n")

    print("\nРезультаты викторины:")
    for i, player in enumerate(players):
        print(f"Игрок {player}: {player_scores[i]} очков")

    max_score = max(player_scores)
    winners = [players[i] for i, score in enumerate(player_scores) if score == max_score]

    if len(winners) == 1:
        print(f"\nПобедитель: Игрок {winners[0]}!")
    else:
        print("\nНичья!")


if __name__ == "__main__":

    question1 = Question("Какое число является корнем квадратным из 81?", ["8", "9", "10", "11"], 2)
    question2 = Question("Какой год был основан OpenAI?", ["2017", "2018", "2019", "2020"], 3)
    # Добавьте еще вопросы по аналогии

    quiz_questions = [question1, question2]

    play_quiz(quiz_questions, players=["1", "2"])
