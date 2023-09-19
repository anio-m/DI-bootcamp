import random
import json
import nltk
from nltk.corpus import words



class AnagramChecker :
 def __init__() :
    with open("/Users/aniomazangia/Desktop/DI-bootcamp/week3/mini-project/word.txt", "r") as word_file :
        words = word_file.readlines()
        
    print(words)



def is_valid_word(Word):
    with open("/Users/aniomazangia/Desktop/DI-bootcamp/week3/mini-project/word.txt", "r") as word_file :
        words = word_file.readlines()
        neword = ''
    for word in words:
        if neword.find(word) == words:
            return True
        else:
            return False
      
print(is_valid_word(""))




# def get_anagrams(word1, word2) :
#    if sorted(word1) == sorted(word2):
#       return "the anagram is "
#    else:
#       print("try again")  
# get_anagrams("asas", "asas")



