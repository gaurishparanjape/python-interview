num = 30
for i in range(2, num + 1):
    Flag = True
    for j in range(2, i):
        if i % j == 0:
            Flag = False
            break
    if Flag == True:
        print(i,end=' ')
