
def gcdOfStrings(str1, str2):

    len1 = len(str1)
    len2 = len(str2)

    print("len1:", len1)
    print("len2:", len2)

    if (len(str1) < len(str2)):
        return gcdOfStrings(str2, str1)

    if str1.equals(str2):
        return str1

    if str1.startswith(str2):
        return gcdOfStrings(str1.substring(len(str2), str2))


str1 = "ABABAB"
str2 = "AB"
gcdOfStrings(str1, str2)
