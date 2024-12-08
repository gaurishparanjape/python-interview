testlist = [1,30,4,2,23]

for i in range(1,len(testlist)):
    j = i
    while j > 0:
        if testlist[j-1] > testlist[j]:
            testlist[j-1],testlist[j] = testlist[j],testlist[j-1]
        else:
            break
        j -= 1
print(testlist)

