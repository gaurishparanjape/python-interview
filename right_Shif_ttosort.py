"""
Given a list, you need to right shift it "k" times such that the resultant list is either in ascending order or descending ordern.
eg:
Input
list [5, 6, 7, 1, 2, 3]
Output:
Sorted list is: [1, 2, 3, 5, 6, 7]
K =  3


Input
[3, 2, 1, 9, 8, 7]
Output
Sorted list is: [9, 8, 7, 3, 2, 1]
K =  3

"""


def check_asc(list1):
    for i in range(len(list1)-1):
        if list1[i+1] < list1[i]:
            return False
    return True


def check_dsc(list1):
    for i in range(len(list1)-1):
        if list1[i+1] > list1[i]:
            return False
    return True

def check(list1):
    k = 0
    print(list1)
    while (check_asc(list1) == False) and (check_dsc(list1) == False):
        temp = list1[0]
        hell = list1.pop(0)
        list1.append(hell)
        k = k+1
        if k > len(list1):
            print("Cannot iterate more")
            break
    print("Sorted list is:",list1)
    print("K = ",k)

list1 = [5, 6,7,1,2,3]
list2 = [3,2,1,9,8,7]
check(list1)
check(list2)