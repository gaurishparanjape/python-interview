import re

# File Read
with open('C:\\Gaurish\\host_entry.txt') as f:
    f_read = f.readlines()

# Match Pattern
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
pattern_string = r"eth\d|lo:"

key = []
ip = []

# sorting matched pattern and display in dictionary.
for line in f_read:
    x = re.findall(pattern, line)
    string_name = re.search(pattern_string, line)
    if (string_name):
        key.append(string_name.group())
    if (len(x)):
        ip.append(x)

# print("key: ", key)
# print("ip: ", ip)

for i in range(len(key)):
    print(key[i], end=" ")
    print(":", ip[i][0])



# [print(f'{key}\t{ip[i][0]}') for key, ip in dict.items()]
