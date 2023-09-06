# fruits = ["apple", "banana", "melon"]
# fav_fruits = fruits
# print(id(fruits) == id(fav_fruits))
# fav_fruits.append("pear")
# print(fruits, fav_fruits)

# make a copy
fruits = ["apple", "banana", "melon"]
fav_fruits = fruits[:]
print(id(fruits) == id(fav_fruits))
fav_fruits.append("pear")
print(fruits, fav_fruits)

# fruits = ["melon", "apple", "banana" ]
# fav_fruits = fruits
# fruits.sort() #sorts the initial list
# print(fruits, fav_fruits)

fruits = ["melon", "apple", "banana" ]
ordered_fruits = sorted(fruits)
print(fruits, ordered_fruits)

# sort() changes the list directly and doesn't return any value, 
# while sorted() doesn't change the list and returns the sorted list.
