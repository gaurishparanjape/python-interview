my_str = 'Harish is the best . Harish loves to do sledging at best . Best that Harish and Anil  play carrom together'
new_str = my_str.split(" ")
dict = {"Harish": "He", "best": "Pandu"}
for key, value in dict.items():
    if key not in new_str:
        continue
    index = new_str.index(key)
    new_str[index] = value
print(new_str)
print(" ".join(new_str))