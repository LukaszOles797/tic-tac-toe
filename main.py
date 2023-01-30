from random import randrange

def draw_division_line():
    for i in range(3):
        print("+", end="")
        for j in range(7):
            print("-", end="")
    print("+")
   
def draw_blank_segment():
    for j in range(3):
        print("|", end="")
        for k in range(7):
            print(" ", end="")
    print("|")
   
def draw_field_segment(field_num):
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" ", end="")
        print(field_num[i], end="")
        for k in range(3):
            print(" ", end="")
    print("|")
   
def display_board(board):
    field = 0
    for i in range(3):
        draw_division_line()
        draw_blank_segment()
        draw_field_segment(board[i])
        draw_blank_segment()
    draw_division_line()
   
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    moved = False
    while moved == False:
        try:
            move = int(input("Enter your move: "))
        except:
            print("Wrong value.")
         
        if move > 0 and move < 10:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = "O"
                        moved = True
        else:
            print("Number out of range. Please enter another number.")
           
    #The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                free_fields.append((i,j))
    return free_fields
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def check_vertical_rows(board, sign):
    for i in range(3):
        x_count = 0
        o_count = 0
        for j in range(3):
            if board[i][j] == "X":
                x_count += 1
            elif board[i][j] == "O":
                o_count += 1
            if o_count == 3:
                sign = "O"
                return sign
            elif x_count == 3:
                sign = "X"
                return sign
    return sign

def check_horizontal_rows(board, sign):
    for i in range(3):
        x_count = 0
        o_count = 0
        for j in range(3):
            if board[j][i] == "X":
                x_count += 1
            elif board[j][i] == "O":
                o_count += 1
            if o_count == 3:
                sign = "O"
                return sign
            elif x_count == 3:
                sign = "X"
                return sign
    return sign
   
def check_diagonal_rows(board, sign):
    x_count = 0
    o_count = 0
    for i in range(3):
        if board[i][i] == "X":
            x_count += 1
        elif board[i][i] == "O":
            o_count += 1;
        if o_count == 3:
            sign = "O"
            return sign
        elif x_count == 3:
            sign = "X"
            return sign
    x_count = 0
    o_count = 0
    for j in range(3):
        if board[j][2-j] == "X":
            x_count += 1
        elif board[j][2-j] == "O":
            o_count += 1
        if o_count == 3:
            sign = "O"
            return sign
        elif x_count == 3:
            sign = "X"
            return sign
    return sign

def victory_for(board, sign):
   
    sign = check_vertical_rows(board, sign)
    if sign == "O":
        print("Human player has won the game.")
        return sign
    elif sign == "X":
        print(("Computer has won the game."))
        return sign
    sign = check_horizontal_rows(board, sign)
    if sign == "O":
        print("Human player has won the game.")
        return sign
    elif sign == "X":
        print(("Computer has won the game."))
        return sign
    sign = check_diagonal_rows(board, sign)
    if sign == "O":
        print("Human player has won the game.")
        return sign
    elif sign == "X":
        print(("Computer has won the game."))
        return sign
       
    free_fields = make_list_of_free_fields(board)
   
    if free_fields == []:
        print("It is a tie.")
        sign = "D"
        return sign
   
    return sign
   
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

def draw_move(board):
    moved = False
    while moved == False:
        comp_move = randrange(9)+1
        for i in range(3):
            for j in range(3):
                if board[i][j] == comp_move:
                    board[i][j] = "X"
                    moved = True
    # The function draws the computer's move and updates the board.

sign = "C"
i = 0
board = [[1,2,3],[4,"X",6],[7,8,9]]
#computer first move - "X" in the middle of the board
display_board(board)
while sign == "C":
    if i % 2 == 0:
        enter_move(board)
        display_board(board)
        sign = victory_for(board, sign)
    else:
        draw_move(board)
        display_board(board)
        sign = victory_for(board, sign)
    i+=1