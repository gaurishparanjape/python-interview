
with open ("File1", "r") as file_1:
    with open("File2", "r") as file_2:
        file2_line = file_2.readlines()
        file1_line = file_1.readlines()

        print(file2_line)
        print(file1_line)
        new_list = []
        if len(file2_line) > len(file1_line):
            for val in file2_line:
                if val not in file1_line:
                    new_list.append(val)
        else:
            for val in file1_line:
                if val not in file2_line:
                    new_list.append(val)


print("".join(new_list))




