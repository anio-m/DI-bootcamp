def check_number (num) :
    if num % 2 == 0 :
        print(f"{num} is even")
    else :
        print(f"{num} is odd")

# check_number(12)
# check_number(34)
# check_number(23)
# check_number(18889)
# check_number(132)

def check_all_numbers (list_numbers) :
    # print(list_numbers)
    for num in list_numbers:
        if num % 2 == 0 :
            print(f"{num} is even")
        else :
            print(f"{num} is odd")

check_all_numbers([12, 34, 76, 89, 120])