import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

# # 🌟 Exercise 1:

def get_words_from_file ():
    with open("/Users/aniomazangia/Desktop/DI-bootcamp/week3/Day4/xp.dc/word.txt", "r") as word_file :
        words_list = []
        for word in word_file.readlines():
          words_list.append(word)
        return words_list
        

# print(get_words_from_file())

def get_random_sentence(lenght):
  
    words_list = get_words_from_file() 
    sentence = ''
    for i in range(lenght):
        word = random.choice(words_list)
        sentence += ''.join(word)
        
    return sentence.lower()

print(get_random_sentence(4))

def main ():
    print("The program uses files/texts outside the program with the help of 'with open' and can change, add and whatever they want.")
num = int(input("what your lenght of your sentence: \n"))
try:
  if not 2 < num > 20:
     raise ValueError("Please enter number between 2 and 20")
except ValueError as error:
   return error
else:
   
   
   
        