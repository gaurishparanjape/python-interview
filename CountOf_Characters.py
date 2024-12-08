from collections import Counter
s = "mary was late"
print(Counter(s))

List = list(s)
uniq = set(List)
for i in uniq:
    print(i, ":", s.count(i), end=', ')


#Mthod 3:
list1 = list(s)
newdict = {}
for i in list1:
    if i in newdict:
        newdict[i] += 1
    else:
        newdict[i] = 1

print(newdict)