num = 6
count = 1
fac = 1
i = 1
if num == 1:
    print("Factorial is 1")
while i < num:
    fac = fac * num
    num = num - 1

print(fac)