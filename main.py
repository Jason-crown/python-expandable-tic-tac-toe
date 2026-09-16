from initialize import game1
import stage
import time
import input
import game_logic

print("\x1b[3J\x1b[H\x1b[2J")
stage.print_board(game1.x, game1.y, game1.board)
input.start_keyboard_listener()

x_pos = 0
y_pos = 0
turn = game1.player_list[0]
turn_index = 0

while True:
    current_key = input.last_key_pressed
    if current_key != "":
        
        if x_pos > 0 and current_key in ("left",'a'):
            print(f"\x1b[2D", end= "", flush = True)
            x_pos -= 1
        elif x_pos < (game1.x-1) and current_key in ("right",'d'):
            print(f"\x1b[2C", end= "", flush = True)
            x_pos += 1
        elif y_pos > 0 and current_key in ("up",'w'):
            print(f"\x1b[1A", end= "", flush = True)
            y_pos -= 1
        elif y_pos < (game1.y-1) and current_key in ("down",'w'):
            print(f"\x1b[1B", end= "", flush = True)
            y_pos += 1
        
        if current_key == "enter" and game1.board[x_pos][y_pos] == game1.space:
            print(f'{turn}\x1b[1D', end= "", flush = True)
            game1.board[x_pos][y_pos] = turn

            if turn_index < len(game1.player_list)-1:
                turn_index += 1
            else:
                turn_index = 0
            turn = game1.player_list[turn_index]
            for players in game1.player_list:
                game_logic.check_win(game1.board, players, game1.x, game1.y)
            
        
        if current_key == "esc":
            game_logic.quit_game()
        input.last_key_pressed = ""
    time.sleep(0.1)