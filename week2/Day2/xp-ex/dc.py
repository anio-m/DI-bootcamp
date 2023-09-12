user_answer = input("give me a number and a length separated by a comma \n")
list_answers = user_answer.split(",")
number = int(list_answers[0])
length = int(list_answers[1])
list_multiples = []

for x in range(length):
    multiple = number * (x+1)
    list_multiples.append(multiple)

print(list_multiples)

user_answer = input("give me a number and a length separated by a comma \n")
list_answers = user_answer.split(",")
number = int(list_answers[0])
length = int(list_answers[1])
new_list_multiples = []

for x in range(1, length+1):
    multiple = number * x
    new_list_multiples.append(multiple)

print(new_list_multiples)