num = 0
list1 = [1,2,4,7,9]
for i in range(len(list1)):
    if list1[i] > num:
        index = i
        break
list1 = list1[:i] + [num] + list1[i:]
print(list1)