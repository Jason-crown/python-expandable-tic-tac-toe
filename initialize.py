import shutil

width, height = shutil.get_terminal_size()
print(f"width = {width}, height = {height}")

x = 3
y = 3
if (width - 5 < x): 
    x = width - 5
    print(f"new width = {width - 5}")
if (height - 5 < y): 
    y = height - 5
    print(f"new height = {height - 5}")

sym = '#'
board = [[sym for _ in range(y)] for _ in range(x)]
