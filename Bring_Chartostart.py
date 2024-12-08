s = "pranav paranjapea"
newlist = []
for char in s:
    if char == 'a':
        newlist = [char] + newlist
    else:
        newlist.append(char)
print(''.join(newlist))