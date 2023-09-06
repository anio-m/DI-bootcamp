# Exercise
#  1. create a function that takes a number as an argument, and check if this number is even or odd
# 2. create a function that takes a list of numbers as an argument, and check if each number is even or odd

# def even_odd (a) :
#     if a % 2 == 0:
#         print("yes is even")
#     else :
#         print ("is odd")

# even_odd(2)

# def check_num (num_list) :
#    for num in num_list: 
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else :
#         print(f"{num} is odd")

# check_num([2, 4, 5, 6,])

# Exercise

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


def price_car (age) :
    if age > 40 :
        return 200
    elif age <= 40 :
        return 300  
    
def price_flight (location) :
    if location == "paris" :
        return 400
    else :
        return 600

def total_allprice () :
    car = price_car(40)
    flight = price_flight("paris")
    total = car + flight
    print(f"your vacation price is {total} dollars")
    
        
total_allprice()        



   