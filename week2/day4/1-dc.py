word = "froggy"
letters_dict = {}

for index,letter in enumerate(word):
    if letter in letters_dict :
        letters_dict[letter].append(index)
    else :
        letters_dict[letter] = [index]

print(letters_dict)

# 1st Loop
# index = 0
# letter = "f"
# letters_dict["f"] = 0
# letters_dict = {
#     "f" : 0
# }

# 1st Loop
# index = 1
# letter = "r"
# letters_dict["r"] = 1
# letters_dict = {
#     "f" : 0,
#     "r" : 1
# }

# 1st Loop
# index = 2
# letter = "o"
# letters_dict["o"] = 2
# letters_dict = {
#     "f" : 0,
#     "r" : 1,
#     "o" : 2
# }

# 1st Loop
# index = 3
# letter = "g"
# letters_dict["g"] = 3
# letters_dict = {
#     "f" : 0,
#     "r" : 1,
#     "o" : 2,
#     "g" : 3
# }

# 1st Loop
# index = 4
# letter = "g"
# letters_dict["g"] = 4
# letters_dict = {
#     "f" : 0,
#     "r" : 1,
#     "o" : 2,
#     "g" : 4
# }

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

items_bought = []
convert_wallet = int(wallet.replace("$", "").replace(",", ""))

for key,value in items_purchase.items():
    convert_value = int(value.replace("$", "").replace(",", ""))
    if convert_value < convert_wallet :
        convert_wallet -= convert_value
        items_bought.append(key)

if len(items_bought) == 0 :
    print("Nothing")
else :
    print(f"I have in my wallet {convert_wallet}")
    items_bought.sort()
    print(f"I bought {items_bought}")
    

    
