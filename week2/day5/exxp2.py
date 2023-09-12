starwars = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    }
]


english = [ 
    {
        "question": "What is yellow in the sky?",
        "answer": "Sun"
    },
    {
        "question": "What is the place where students learn",
        "answer": "Classroom"
    }
]



def check_answers (data) :
    number_correct_answers = 0
    number_incorrect_answers = 0
    list_wrong_answers = []
    for quizz in data :
        user_answer = input(quizz["question"])
        if user_answer == quizz["answer"]:
            number_correct_answers += 1
        else :
            number_incorrect_answers += 1
            new_quizz = quizz.copy() #make a copy of the dictionary
            new_quizz["user_answer"] = user_answer
            list_wrong_answers.append(new_quizz)

check_answers(starwars)
check_answers(english)