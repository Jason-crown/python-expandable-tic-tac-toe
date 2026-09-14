import sys
from initialize import game1

def check_win(board, player, x, y):
    for span in range(abs(y-x)+1):
        for types in range(2):
            if x > y and span > 0:
                span *= -1
            line_check(types, player, board, x, y, span)
    if not any(game1.space in row for row in board):
        print("\x1b[3J\x1b[H\x1b[2J Tie")
    

def line_check(type, player, board, x, y, span):
    
    line_set = diagonal_set = 0
    sub_board = [[row[i] for row in board] for i in range(len(board[0]))]
    line_list = [player]*game1.win_amount
    diagonal_list = []
    anti_diagonal_list = []

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
            
            if columns == diagonal_logic+span:
                if type == 0:
                    diagonal_list.append(board[columns][diagonal_logic+span])
                else :
                    anti_diagonal_list.append(board[columns][diagonal_logic+span])

                if board[rows][columns] == player:
                    diagonal_set += 1
                if ("".join(line_list) in "".join(anti_diagonal_list) or "".join(line_list) in "".join(diagonal_list)) == True:
                    print(f" {player} WINS2")
                    
            
            
                
        if game1.win_amount in (line_set, diagonal_set) or line_set > game1.win_amount:
            print(f"\x1b[3J\x1b[H\x1b[2J {player} WINS3")
        line_set = 0



def quit_game():
    print("\n\tQuitting")
    sys.exit(0)
        

                
