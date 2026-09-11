from initialize import game1
import sys

def check_win(board, player):
    horizontal_check = vertical_check = diagonal_check = anti_diagonal_check = 0

    for rows in range(0, game1.x):
        for columns in range(0, game1.y):
            if board[rows][columns] == player:
                vertical_check += 1
            if (columns == rows) and board[rows][columns] == player:
                diagonal_check += 1
            if board[columns][rows] == player:
                horizontal_check += 1
            if rows == abs(game1.x-(columns+1)) and board[columns][rows] == player:
                anti_diagonal_check += 1

        if min(game1.x, game1.y) in (vertical_check, horizontal_check, diagonal_check, anti_diagonal_check):
            print("\x1b[3J\x1b[H\x1b[2J")
            print(f"{player} WINS")
            sys.exit(0)

        horizontal_check = vertical_check = 0
    

        

                
