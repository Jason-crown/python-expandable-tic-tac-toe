import shutil
from dataclasses import dataclass, field

width, height = shutil.get_terminal_size()
print(f"width = {width}, height = {height}")

x_pos = 0
y_pos = 0

@dataclass
class game:
    x: int = 3
    y: int = 3
    win_amount: int = 3 # this is a place holder value 
    player_list: list[str] = field(default_factory=lambda: ['x', 'y']) # add to this list to get more players
    space: str = '#'
    board: list[list[str]] = field(init=False)
    def __post_init__(self):
        if (width/2 - 5 < self.x): 
            self.x = int(width/2) - 5
            print(f"new width = {width - 5}")
        if (height - 5 < self.y): 
            self.y = height - 5
            print(f"new height = {height - 5}")
        self.win_amount = min(self.x, self.y)
        self.board = [[self.space for _ in range(self.y)] for _ in range(self.x)]
game1 = game()

