from initialize import game1
import stage
import time
import input
import game_logic

print("\x1b[3J\x1b[H\x1b[2J")
stage.print_board(game1.x, game1.y, game1.board)
input.start_keyboard_listener()

print(f"\x1b[{5};{3}H", end= "", flush = True)
x_pos = 0
y_pos = 0
turn = 'x'

while True:
    current_key = input.last_key_pressed
    if current_key != "":
        if x_pos > 0 and current_key == "left":
            print(f"\x1b[2D", end= "", flush = True)
            x_pos -= 1
        elif x_pos < (game1.x-1) and current_key == "right":
            print(f"\x1b[2C", end= "", flush = True)
            x_pos += 1
        elif y_pos > 0 and current_key == "up":
            print(f"\x1b[1A", end= "", flush = True)
            y_pos -= 1
        elif y_pos < (game1.y-1) and current_key == "down":
            print(f"\x1b[1B", end= "", flush = True)
            y_pos += 1
        
        if current_key == "enter" and game1.board[x_pos][y_pos] == game1.space:
            print(f'{turn}\x1b[1D', end= "", flush = True)
            game1.board[x_pos][y_pos] = turn

            if turn == 'x':
                turn = 'o'
            else :
                turn = 'x'
            game_logic.check_win(game1.board, 'x')
            game_logic.check_win(game1.board, 'o')
        
        if current_key == "esc":
            print("\nQuitting")
            break
        input.last_key_pressed = ""
    time.sleep(0.1)