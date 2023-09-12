data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def check_answers () : # the name function
    number_correct_answers = 0
    number_incorrect_answers = 0
    list_wrong_answers = []

    print("\n ---- The quizz starts ----")
    for quizz in data : #Checks all the user's answers
        user_answer = input(quizz["question"]) #box to enter the answer
        if user_answer.lower() == quizz["answer"].lower(): 
            number_correct_answers += 1 # If the answer is the same, add it
        else :
            number_incorrect_answers += 1 # If not then add a wrong answer
            new_quizz = quizz.copy() #make a copy of the dictionary
            new_quizz["user_answer"] = user_answer
            list_wrong_answers.append(new_quizz)
    
    inform_user(number_correct_answers, number_incorrect_answers, list_wrong_answers)

def inform_user (correct, incorrect, wrong_answers) : # the name function
    print("\n ----------------------------")
    print(f"You have {correct} correct answers") # Returns the correct answer to the user
    print(f"You have {incorrect} incorrect answers") # Returns an incorrect answer to the user
    for global_answer in wrong_answers : # A loop that checks all the user's answers
        print(f'The question was {global_answer["question"]}') #Checks the user's answer and returns an answer to him
        print(f'Your answer was {global_answer["user_answer"]}')# Checks the user's answer and returns an answer to him
        print(f'Your got it wrong, the correct answer is {global_answer["answer"]}')
    
    print("\n --------------------")
    if incorrect > 3 :
        print(" YOU GOT MORE 3 ANSWERS WRONG Play Again")
        check_answers()
    else :
        print("Good Job - YOU DONT NEED TO REDO THE GAME")

check_answers()