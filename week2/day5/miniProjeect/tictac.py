
board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]

def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

display_board()        

def player_input ():
   row = int(input("What your row number ? the options is between (0 - 2:)\n "))
   colum = int(input("What your colum number ? the options is between 0 - 2:\n "))
   if 0 <= row <= 2 and 0 <= colum <= 2:
    return row, colum
   else:
        print("This number is not valid! Please enter a valid number again")

player_input ()

