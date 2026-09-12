import sys
from initialize import game1

def check_win(board, player, x, y):

    if player == game1.player2: 
        not_player = game1.player1 
    else:
        not_player = game1.player2
    
    horizontal_check = vertical_check = diagonal_check = anti_diagonal_check = 0

    if not any(game1.space in row for row in board):
        print("\x1b[3J\x1b[H\x1b[2J Tie")

    for rows in range(0, x):
        for columns in range(0, y):
            if board[rows][columns] == player:
                vertical_check += 1
            if board[rows][columns] == game1.space or board[rows][columns] == not_player:
                vertical_check = 0
            if (columns == rows) and board[rows][columns] == player:
                diagonal_check += 1

        if min(x, y) in (vertical_check, horizontal_check, diagonal_check, anti_diagonal_check):
            print(f"\x1b[3J\x1b[H\x1b[2J {player} WINS1")

        horizontal_check = vertical_check = 0

    for columns in range(0, y):
        for rows in range(0, x):
            if board[rows][columns] == player:
                horizontal_check += 1
            if board[rows][columns] == game1.space or board[rows][columns] == not_player:
                horizontal_check = 0
            if columns == abs(x-(rows+1)) and board[rows][columns] == player:
                anti_diagonal_check += 1

        if min(x, y) in (vertical_check, horizontal_check, diagonal_check, anti_diagonal_check):
            print(f"\x1b[3J\x1b[H\x1b[2J {player} WINS2{vertical_check, horizontal_check, diagonal_check, anti_diagonal_check}")

        horizontal_check = vertical_check = 0
    
def quit_game():
    print("\n\tQuitting")
    sys.exit(0)
        

                
