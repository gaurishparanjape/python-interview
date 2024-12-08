
def countLetters(s, ndict):
    for char in s:
        if char in ndict.keys():
            ndict[char] += 1
        else:
            ndict[char] = 1
    return ndict


s = "geeksforgeeks"
ndict = {}

print(countLetters(s, ndict))