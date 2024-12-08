
def inner_for(i, flag):
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            flag = 0
            break
    return flag

def prime_interval(start, end):
    final_prime_list = []
    for i in range(start, end+1):
        flag = 1
        flag = inner_for(i, flag)
        if flag == 1:
            final_prime_list.append(i)

    print(final_prime_list)

prime_interval(1,29)