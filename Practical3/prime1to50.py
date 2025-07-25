print("following are the prime from 1 to 50")
for i in range(2,51):
    flag = True
    for j in range(2,i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i,end=' ')