
import re

string = "Naman25abcd200efg25abd7"

numbers = re.findall(r'\d+', string)
print(numbers)
sum = 0
for i in numbers:
    sum += int(i)
print(sum)