path = "D:/Android"
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print(onlyfiles)