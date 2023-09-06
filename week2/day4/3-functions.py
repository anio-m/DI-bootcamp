# function is a piece of code
# enclose a program that we reuse
# that contains a program
# that we use
# --> avoid repetition
# call the function --> work


# Syntax

# create a function
def say_hello () :
    print("hello")

# invokation
# calling
say_hello()
say_hello()
say_hello()
say_hello()

# arguments and parameters
# whatever is in the creation of the function is called a parameter
# a box waiting to be filled with info
# name of the parameter doesnt mater

def say_hello (username) :
    print("hello " + username)

# invokation
# calling the function
# execute the function
# argument in the invokation
say_hello("John")
say_hello("Lea")
say_hello("Denis")


def say_bye () :
    print("bye")

# i execute the function only if i call it
say_bye()

def calculate (a, b, operator) :
    if operator == "+" :
        total = a + b
        print(total)
    elif operator == "-":
        total = a - b
        print(total)


calculate(2,4,"+")
calculate(20,40,"-")
