#default parameters
# are used only if the argument is not passed
def check(a,b,operator = "+") :
    if operator == "+" :
        total = a + b
        print(total)
    elif operator == "-":
        total = a - b
        print(total)
    else :
        print("nothing")

# check(4,5) --> 9
# check(4,5, "-") --> -1

# reuse function
# code needs to be enclosed
# return data

# def get_fullname (firstname, lastname) :
#     fullname = f"{firstname} {lastname}"
#     return fullname

# print(get_fullname("John", "Smith"))
# # print(fullname)
# # print("John Smith")

# return means that the function has now a result

# def get_fullname (firstname, lastname) :
#     fullname = f"{firstname} {lastname}"
#     # local variable

# print(fullname) #NameError: name 'fullname' is not defined


# return data
# i will have access to it oustide the function

# if a function doesnt return anything then it doesnt have a result
# the function returns None

def get_fullname (firstname, lastname) :
    fullname = f"{firstname} {lastname}"
    return fullname
    # print("hello") not executed

username = get_fullname("John", "Smith")
sentence = f"Hi user your fullname is {username}"
print(sentence)

# return has 2 goals
# return a value, so that we can use it outside of the function
# stop the function

# def get_fullname (firstname, lastname) :
#     if firstname == "Sara" :
#         return  
#         print("test:test")
#     else :
#         return firstname + " " + lastname

# username = get_fullname("John", "Smith")
# sentence = f"Hi user your fullname is {username}"
# print(sentence)


#2 functions
# one that find the sum out a list of numbers
# second that receive this sum and multiply it by the taxes 1.17

# prices = [32,24,16]

# def find_sum () :
#     total = 0
#     for price in prices :
#         total += price
#     return total

# def multiply_taxes () :
#     final_total = find_sum() * 1.17
#     print(final_total)

# multiply_taxes()
    


prices = [32,24,16]

def find_sum () :
    total = 0
    for price in prices :
        total += price
    if total > 100 :
        return ("the price is high", total)
    else :
        return ("the price is low", total)

def inform_user () :
    result = find_sum()
    sentence = f"hello user, {result[0]} - your total is {result[1]}"
    print(sentence)

inform_user()
                              





def multiply_taxes () :
    final_total = find_sum() * 1.17
    print(final_total)

multiply_taxes()


# # project vacation
# 1st function - get_price_car
# receive the age of the user 
# and if the user is > 40
#     --> 200
# if the user is < 40
#     --> 300

# 2nd function - get_price_flight
# receive a destination from the user
# if the destinatation is Paris
#     --> 400
# else
#     --> 600

# 3rd function
# is going to use the result from the 2 functions above
# and inform the user of the total price of the vacation

def get_price_car (age_user) :
    if age_user > 40 :
        return 200
    else :
        return 300
    
def get_flight_price(destination):
    if destination == "Paris" :
        return 400
    else :
        return 600

def inform_user_vacation () :
    age = int(input("what is your age \n")) #45
    city = input("where do you go \n") #"tlv"

    price_car = get_price_car(age) #get_price_car(45)
    flight_price = get_flight_price(city) # get_flight_price("tlv")

    total = price_car + flight_price
    print(f"your vacation will cost {total} dollars")

inform_user_vacation()

def get_price_car () :
    age = int(input("what is your age \n")) #45
    if age > 40 :
        return 200
    else :
        return 300
    
def get_flight_price():
    city = input("where do you go \n") #"tlv"
    if city == "Paris" :
        return 400
    else :
        return 600

def inform_user_vacation () :
    total = get_price_car() + get_flight_price()
    print(f"your vacation will cost {total} dollars")

inform_user_vacation()