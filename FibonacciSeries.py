num = 20
prev = 0
curr = 1

while prev <= num:
    print(prev)
    nextnum = prev + curr
    prev = curr
    curr = nextnum


def fibonacci(n):
    prev = 0
    present = 1
    while prev <= n:
        next_num = present + prev
        prev = present
        present = next_num