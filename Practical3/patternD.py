rows = 7
for i in range(rows):
    for j in range(5):
        if (i == 0 and j < 4):
            print("*",end='')
        elif (i == 6 and j < 4):
            print("*",end="")
        elif (j == 0):
            print("*",end='')
        elif (j == 4 and (i >= 1 and i <= 5)):
            print("*",end='')
        else:
            print(' ',end='')
    print()