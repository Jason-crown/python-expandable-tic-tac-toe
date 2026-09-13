x = 5
y = 3
for span in range(abs(y-x)+1):
    for types in range(2):
        if x > y and span > 0:
            span *= -1
        print(f"{types, span}")