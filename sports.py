import pickle

quiz_questions = [
   {
       "question": "Which country won the FIFA World Cup in 2018?",
       "options": ["France", "Brazil", "Germany", "Spain"],
       "answer": "France"
   },
   {
       "question": "Who holds the record for the most home runs in Major League Baseball?",
       "options": ["Babe Ruth", "Barry Bonds", "Hank Aaron", "Alex Rodriguez"],
       "answer": "Barry Bonds"
   },
   {
       "question": "Who won the NBA Finals in 2020?",
       "options": ["Los Angeles Lakers", "Golden State Warriors", "Toronto Raptors", "Miami Heat"],
       "answer": "Los Angeles Lakers"
   }
]

def run_quiz():
   score = 0

   for question in quiz_questions:
       print(question["question"])
       for i, option in enumerate(question["options"]):
           print(f"{i+1}. {option}")

       user_answer = input("Enter your answer (1-4): ")

       if user_answer == str(question["options"].index(question["answer"]) + 1):
           score += 1

   print(f"\nQuiz completed! Your score is {score}/{len(quiz_questions)}.")
   
   if score < 3:
      print("Shame on you, you didn't get full points!!!! You simply must try again.")
   elif score == 3:
      print("Good work.")
   else:
      print("You're all done!")

def save_quiz():
   with open("quiz.pickle", "wb") as file:
       pickle.dump(quiz_questions, file)
   print("Quiz saved successfully!")

def load_quiz():
   global quiz_questions
   try:
       with open("quiz.pickle", "rb") as file:
           quiz_questions = pickle.load(file)
       print("Quiz loaded successfully!")
   except FileNotFoundError:
       print("No saved quiz found.")

def main_menu():
   while True:
       print("\n--- Sports Quiz ---")
       print("1. Start Quiz")
       print("2. Save Quiz")
       print("3. Load Quiz")
       print("4. Exit")
       choice = input("Enter your choice (1-4): ")

       if choice == "1":
           run_quiz()
       elif choice == "2":
           save_quiz()
       elif choice == "3":
           load_quiz()
       elif choice == "4":
           break
       else:
           print("Invalid choice. Please try again.")

main_menu()

print("Good job! Thank you for playing this game. Brought to you by Hansley, Miles, Rachel, Benji, Patrick.")
