a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]
c = []
max = 0
if len(a) > len(b):
    max = len(a)
else:
    max = len(b)
i = 0
while a and b:
    if a[i]>b[i]:
        c.append(a[0])
    else:
        c.append(b[i])
    i = i+1
    if i == max:
        break

print(c)

print(c+a+b)
