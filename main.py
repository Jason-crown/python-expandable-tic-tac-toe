from initialize import game1, x_pos, y_pos
from time import sleep
import stage
import input


stage.print_board(game1.x, game1.y, game1.board)
input.start_keyboard_listener()


while True:

    current_key = input.last_key_pressed

    if current_key != "":
        x_pos, y_pos = input.game_options(x_pos, y_pos, current_key)
        input.last_key_pressed = ""

    sleep(0.1)