def print_board(x, y, board):
    print("\x1b[3J\x1b[H\x1b[2J")
    print(f'\n\n+{'-'*(2*x+1)}+')
    for y_pos in range(0, y):
        print("| ", end ="")
        for x_pos in range(0, x):
            print(f"{board[x_pos][y_pos]} ", end = "")
        print("|")
    print(f"+{'-'*(2*x+1)}+", end = "")
    print(f"\x1b[{5};{3}H", end= "", flush = True)