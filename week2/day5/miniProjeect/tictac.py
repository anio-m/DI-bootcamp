
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

def update_board(row, column, player):
    if board[row][column] == ' ':
        board[row][column] = player
        return True
    else:
        return False
    
def check_winner():

    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None    

