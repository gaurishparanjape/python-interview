def reverseWord(s):
    ns = s.split(" ")
    nw = []
    for i in ns:
        nw.append("".join(i[::-1]))

    print(nw)




s = "Hey this is a statement to reverse"
reverseWord(s)