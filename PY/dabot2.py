import os

path = "directory/"

dirs = os.listdir(path)

for i in dirs:
    i = path+i
    f = open(i, "r")
