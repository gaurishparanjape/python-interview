list_new = [1, 2, 3, 4, 2, 19, 20, 21, 22, 32, 35]
count = 0

arr_count = []
for i in range(len(list_new)-1):
    calculate = list_new[i+1] - list_new[i]
    if calculate == 1:
        count +=1
    else:
        arr_count.append(count+1)
        count = 0
print(max(arr_count))