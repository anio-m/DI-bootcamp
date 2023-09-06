# # # exercise
# # # ask the user for the fruit he wants
# # # depending on the fruit we show him the price
# # # don't use conditionals

# prices = {
#     "apple" : 2,
#     "banana" : 5,
#     "orange" : 1
# }

# my_fruit = input("what fruit do you wont ? \n")
# print(f"the price for the fruit {my_fruit} is {prices[my_fruit]} dollars")

# # exercise

# # create a new list that only contains the uppercased words
# # words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']


# list_words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
# new_list = []

# for word in list_words :
#     if word.isupper():
#         new_list.append(word)
#     # else :
#     #     print(f"the word {word} is not uppercased")

# print(new_list)



# Exercise 3
# Print the total duration of the playlist

playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}
total = 0
for music in playlist["songs"] :
    total += music["duration"]
    print(total)