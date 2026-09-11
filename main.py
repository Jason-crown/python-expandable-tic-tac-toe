from initialize import x, y, board, size, sym
import stage
import time
import input
import game_logic

print("\x1b[3J\x1b[H\x1b[2J")
stage.print_board(x, y, board)
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
        elif x_pos < (x-1) and current_key == "right":
            print(f"\x1b[2C", end= "", flush = True)
            x_pos += 1
        elif y_pos > 0 and current_key == "up":
            print(f"\x1b[1A", end= "", flush = True)
            y_pos -= 1
        elif y_pos < (y-1) and current_key == "down":
            print(f"\x1b[1B", end= "", flush = True)
            y_pos += 1
        
        if current_key == "enter" and board[x_pos][y_pos] == sym:
            print(f'{turn}\x1b[1D', end= "", flush = True)
            board[x_pos][y_pos] = turn

            if turn == 'x':
                turn = 'o'
            else :
                turn = 'x'
            game_logic.check_win(board, 'x')
            game_logic.check_win(board, 'o')
        
        if current_key == "esc":
            print("\nQuitting")
            break
        input.last_key_pressed = ""

    #print(".", end="", flush = True)
    time.sleep(0.1)