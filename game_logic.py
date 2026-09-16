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

    sub_board = [[row[i] for row in board] for i in range(len(board[0]))]
    line_list = [player]*game1.win_amount
    anti_diagonal_list = diagonal_list = []

    for set_1 in range(0, y if type else x):
        for set_2 in range(0, x if type else y):
            column = set_1 if type else set_2
            if column == set_1 and type == 0:
                diagonal_list.append(board[set_1+span][column])
            if column == set_2 and type == 1:
                anti_diagonal_list.append(board[abs(x-(set_2+1))+span][column])
            board_list = ["".join(board[column]), "".join(sub_board[column]),"".join(diagonal_list),"".join(anti_diagonal_list)]
            for i in range(4):
                if ("".join(line_list) in "".join(board_list[i])) == True:
                    win_game(player)
            
def win_game(player):
    print(f" \x1b[{5+game1.y};{3+int(game1.x/2)}H{player} WINS")


def quit_game():
    print("\n\tQuitting")
    sys.exit(0)
        

                
