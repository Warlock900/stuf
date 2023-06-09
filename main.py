import pickle

count = 0


with open("questions.py", "rb") as file:
    previous_Qs = pickle.load(file) 
    if previous_Qs == None:
        previous_Qs = {
            "questions" : "none"
        }
    else:
        print("here are previous questions added by users...")
        for key, value in previous_Qs.items():
            print(previous_Qs[key])
            count += 1



qtoadd = input("what question would you like to add to the list of questoins?")

previous_Qs[str(count)] = qtoadd

with open("questions.py", "wb") as file:
    pickle.dump(previous_Qs, file)