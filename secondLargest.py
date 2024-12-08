random_list = [312,13,12,44,512,5,12]

largest = 0

second_largest = 0

for i in random_list:
    if i > largest:
        second_largest = largest
        largest = i

    elif i>=second_largest and i< largest:
        second_largest = i
    else:
        second_largest = second_largest
        largest = largest


print(second_largest)
print(largest)