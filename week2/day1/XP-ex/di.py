# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

# Then, print the first and last characters of the given text.

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "HelloWorld"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# HelloWorld


# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod

string = str(input("put string The string must be exactly 10 characters long :"))
if len(string) < 10:
    print("The string is not long enough") 
elif len(string) >10:
    print("The string is too long")  
elif len(string) == 10:
    print("The string is perfect")

print(f"the last letter is {string[-1]}")
print(f"the fist letter is {string[0]}")

world = ""
for letter in string:
    world += string
    print(world)
