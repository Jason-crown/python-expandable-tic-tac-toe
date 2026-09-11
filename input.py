from pynput import keyboard

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

