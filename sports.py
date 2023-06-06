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

quiz = Quiz()

quiz.add_question("What's the diameter of a basketball hoop in inches?", "18")
quiz.add_question("The Olympics are held every how many years?", "4")
quiz.add_question("What do the rings in the Olympics represent", "The Continents".lower())
quiz.add_question("What is the national sport of Canada?", "Lacrosse".lower())
quiz.add_question("What country has competed the most times in the Summer Olympics yet hasn't won a gold medal?", "Philippines".lower())
quiz.add_question("In what game is love a score?", "Tennis".lower())
quiz.add_question("What type of race is the Tour de France?", "Biking".lower())
quiz.add_question("How long is a marathon?", "26.2 Miles".lower())
quiz.add_question("In football, how many points does a touchdown hold?", "Six".lower())

while True:
    print("Welcome to the Sports Trivia Quiz!")
    print("1. Start Quiz")
    print("2. View High Scores")
    print("3. Quit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter your name: ")
        quiz.run_quiz()
        quiz.save_score(name)
        print("Quiz completed. Your score has been saved.")
    elif choice == "2":
        quiz.show_high_scores()
    elif choice == "3":
        print("Thank you for playing! Brought to you by Miles, Hansley, Benji, Rachel, and Patrick")
        break
    else:
        print("You can't do that. Please try again.")
