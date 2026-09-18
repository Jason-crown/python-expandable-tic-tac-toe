from pynput import keyboard
from initialize import game1
import game_logic
last_key_pressed = ""


def on_press(key):
    global last_key_pressed

    try:
        last_key_pressed = key.char
    except AttributeError:
        last_key_pressed = key.name


def start_keyboard_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()


def game_options(x_pos, y_pos, current_key):
    x_pos, y_pos = game_movement(x_pos, y_pos, current_key)
    
    if current_key == "enter" and game1.board[x_pos][y_pos] == game1.space:
        print(f'{game_logic.turn}\x1b[1D', end= "", flush = True)
        game1.board[x_pos][y_pos] = game_logic.turn
        game_logic.turn_logic()
    
        for players in game1.player_list:
            game_logic.check_win(game1.board, players, game1.x, game1.y)
                
    if current_key == "esc":
        game_logic.quit_game()
    return x_pos, y_pos


def game_movement(x_pos, y_pos, current_key):
    match current_key:
        case "left" | 'a' if x_pos > 0:
            print(f"\x1b[2D", end= "", flush = True)
            x_pos -= 1
        case "right" | 'd' if x_pos < (game1.x-1):
            print(f"\x1b[2C", end= "", flush = True)
            x_pos += 1
        case "up" | 'w'if y_pos > 0:
            print(f"\x1b[1A", end= "", flush = True)
            y_pos -= 1
        case "down" | 's' if y_pos < (game1.y-1):
            print(f"\x1b[1B", end= "", flush = True)
            y_pos += 1            
    return x_pos, y_pos