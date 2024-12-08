# Method 1
List1 = [1,2,5,7,10,6,5]
sortedlist = sorted(List1)
print(sortedlist[len(sortedlist) - 2])

# Method 2 without sorting
List2 = [9,2,5,7,10,6,8,5]
greatest = 0
secondgreatest = 0
for i in List2:
    if i > greatest:
        secondgreatest = greatest
        greatest = i
    elif i < greatest and i > secondgreatest:
        secondgreatest = i
print("greatest: " + str(greatest))
print("second greatest: " + str(secondgreatest))