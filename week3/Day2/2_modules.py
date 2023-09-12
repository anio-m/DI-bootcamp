# import random
# # import all the methods of the random module

# number = random.randint(1,10)
# print(number)



# import a specific function
from random import randint, shuffle

number = randint(1,10)
print(number)

list = ["apple", "banana", "pear"]
shuffle(list)
print(list)