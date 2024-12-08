"""Given a a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
Input/Output

[time limit] 4000ms (py)
[input] array.string picture"""




def addBorder(picture):
    # slightly more compley length computation, will work for ragged text as well
    maxL = max(len(x) for x in picture)
    patt = "*{:<"+str(maxL)+"}*"   # left justified by maxL , see link below
    rv = []
    rv.append('*'*(maxL+2))    # top border

    for t in picture:
        rv.append(patt.format(t)) # text + adornment

    rv.append('*'*(maxL+2))    # bottom border

    return rv


def anothermethod(picture):
    border = "*"
    output = []

    maxLen = max (len(i)for i in picture)
    output.append(border * (maxLen+2))

    for i in range(len(picture)):
        output.append(border + picture[i] + border)

    output.append(border * (maxLen+2))

    return output

#print(addBorder( ["abc", "defgh","i"]))

print(anothermethod(["a", "acde", "a"]))