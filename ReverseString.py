s = "pranav"
rev1 = s[::-1]
print(rev1)

rev = ''
for cnt in range(len(s), 0, -1):
    rev = rev + s[cnt-1]
print(rev)

chars = list(s)
for i in range(len(s) // 2):
    tmp = chars[i]
    chars[i] = chars[len(s) - i - 1]
    chars[len(s) - i - 1] = tmp
print(''.join(chars))
