# Exercise 2 : What Is The Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

numer = int(input("What month do you want?"))
if 3 <= numer <= 5 :
    print("Spring")

elif 6 <= numer <= 8 :
     print("Summer")
elif 9 <= numer <= 11:
    print("Autumn")
elif numer <2 or numer == 12 :
    print("Winter")    
    
else:
    print("Error")