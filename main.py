import pickle

with open("questions.py", "rb") as file:
    previous_Qs = pickle.load(file) 
    if previous_Qs == None:
        print()
    else:
        print("here is the last question added by a users...")
        print(previous_Qs)

class Quiz():
    def add_user_question(self):
        qtoadd = input("What question would you like to add to the quiz?")
        with open("questions.py", "wb") as file:
            pickle.dump(qtoadd, file)
    
quiz = Quiz()

quiz.add_user_question()
