import sys
from initialize import game1

def check_win(board, player, x, y):
    if not any(game1.space in row for row in board):
        print("\x1b[3J\x1b[H\x1b[2J Tie")
    for span in range(abs(y-x)+1):
        for types in range(2):
            if x > y and span > 0 and types == 1:
                span *= -1
            line_check(types, player, board, x, y, span)

def line_check(type, player, board, x, y, span):
    diagonal_list = []
    anti_diagonal_list = []
    line_set = diagonal_set = 0
    sub_board = [[row[i] for row in board] for i in range(len(board[0]))]
    line_list = [player]*game1.win_amount

    if type == 0:
        upper = x
        lower = y
    else:
        upper = y
        lower = x
        
    for set_1 in range(0, upper):
        for set_2 in range(0, lower):

            if type == 0:
                rows = set_1
                columns = set_2
                diagonal_logic = set_1
            else:
                rows = set_2
                columns = set_1
                diagonal_logic = abs(x-(set_2+1))

            if board[rows][columns] == player:
                line_set += 1

            if ("".join(line_list) in "".join(board[rows]) or "".join(line_list) in "".join(sub_board[columns])) == False:
                line_set = 0
            else:
                print(f" {player} WINS1")

            if columns == diagonal_logic and type == 0: 
                diagonal_list.append(board[diagonal_logic+span][columns])
                #print(columns, diagonal_logic+span)
            if columns == set_2 and type == 1:
                #print(columns, diagonal_logic+span)
                anti_diagonal_list.append(board[diagonal_logic+span][columns])

            if columns == diagonal_logic+span and board[rows][columns] == player:
                diagonal_set += 1
                
        if game1.win_amount in (line_set, diagonal_set) or line_set > game1.win_amount:
            print(f" {player} WINS{anti_diagonal_list, diagonal_list}")
        line_set = 0



def quit_game():
    print("\n\tQuitting")
    sys.exit(0)
        

                
