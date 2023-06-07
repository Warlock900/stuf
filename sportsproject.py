import pickle

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, answer):
        self.questions.append((question, answer))

    def run_quiz(self):
        for question, answer in self.questions:
            user_answer = input(question + " ")
            if user_answer.lower() == answer.lower():
                self.score += 1

    def save_score(self, name):
        try:
            with open("high_scores.pkl", "rb") as file:
                high_scores = pickle.load(file)
        except FileNotFoundError:
            high_scores = []

        high_scores.append((name, self.score))

        with open("high_scores.pkl", "wb") as file:
            pickle.dump(high_scores, file)

    def show_high_scores(self):
        try:
            with open("high_scores.pkl", "rb") as file:
                high_scores = pickle.load(file)
        except FileNotFoundError:
            print("No high scores yet.")
            return

        print("High Scores:")
        for name, score in high_scores:
            print(name + ": " + str(score))
