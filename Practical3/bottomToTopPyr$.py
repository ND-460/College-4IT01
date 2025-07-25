rows = 5
for i in range(rows, 0, -1):
    spaces = rows - i
    symbols = 2 * i - 1
    print(' ' * spaces + '$' * symbols)
