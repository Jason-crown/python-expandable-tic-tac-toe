horizontal_check = 0
for rows in range(0, 5):
    for columns in range(0, 5):
        print(f"{rows}, {columns}")
        horizontal_check += 1
    print(f"----{horizontal_check}")
    horizontal_check = 0