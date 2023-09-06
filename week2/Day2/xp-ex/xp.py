# # 🌟 Exercise 1 :

# my_fav_numbers = {10, 20 ,30 ,40}
# myall_fav_numbers = [50, 60]
# my_fav_numbers.update(myall_fav_numbers)
# print(my_fav_numbers)

# my_fav_numbers = set(list(my_fav_numbers)[:-1])
# print(my_fav_numbers)

# friend_fav_numbers = {2 ,4 ,8 ,23}

# our_fav_numbers = friend_fav_numbers.union(my_fav_numbers)
# print(our_fav_numbers)

# 🌟 Exercise 2 :
# No, you can't because tuples are immutable and therefore the sum can not be modified.
# You will have to create a new tuple.

# # 🌟 Exercise 3 :

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.append("Kiwi")
# print(basket)
# basket.insert(0, "Apples")
# print(basket)

# Apples = basket.count("Apples")
# print(Apples)

# basket.clear()
# print(basket)


# # 🌟 Exercise 4 :

# An integer is a number without a decimal point like (5, 4 ,2). A float is a floating-point number, which means it is a number that has a decimal place like (2.1, 43.22, 12.12).

# arange() method.

# listfloating = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5] 
# list_float = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

# # 🌟 Exercise 5 :

# count = 0
# for number in range(1, 21) :
#     if number % 2 == 0 :
#         print(number)


# # 🌟 Exercise 6 :
# myname = "aviho"
# num = ""
# while True:
#     namechamp = input("what your name ?")
#     if myname == namechamp:
#      print("bingo")
#      break


# # 🌟 Exercise 7 :

# favorite_fruit = input("what your favorite fruit ? if you have several fruit seperate by a space?")
# print(favorite_fruit)

# new_fruit = favorite_fruit.split()
# print(new_fruit)

# favorite = input("what your favorite fruit")
# if favorite in favorite_fruit :
#     print("You chose one of your favorite fruits! Enjoy!")

# else :
#     print("ou chose a new fruit. I hope you enjoy")
 


# # # 🌟 Exercise 8 :

list_topping = []
price = 10
while True:
     user_topping = input("what your topping you wont in pizza ?\n")
     if user_topping == 'quit' :
          print("your pizza will be ready in 10 min")
          prompt  = "bye"
          break
     else:
          list_topping.appned(user_topping)
          price +=2.5
          print(f"you added{user_topping} to your pizza")

     print(f'you add{" ".join(list_topping)} so your total price is {price}')  



#  # # 🌟 Exercise 9 :    

age = 0

price_ticket = int(input("what your age?"))

if price_ticket <+ 3:
      print("the ticket is free")

elif 3<=price_ticket<=12:
     print("the price ticket is 10$")

elif price_ticket>12:
     print("the price ticket is 15$")
       


    
     

