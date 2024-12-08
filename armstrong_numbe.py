#Armstrong Number
def armstrongNumber(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        return "{} is armstrong number ".format(num)
    else:
        return "{} is not armstrong number ".format(num)


print(armstrongNumber(153))
print(armstrongNumber(111))

