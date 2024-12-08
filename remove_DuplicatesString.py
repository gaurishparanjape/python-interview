
def removedup(s, ns):
    for char in s:
        if char not in ns:
            ns = ns + char
    return ns

s = "geeksforgeeks"
ns = ""
print(removedup(s, ns))



