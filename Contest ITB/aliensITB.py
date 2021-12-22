mylist = []
num = 0
while True:
    x = [int(x) for x in input().split(" ")]
    for j in x:
        if j == 0:
            num = 1
            x.remove(j)
    if num == 1:
        break
for i in x:
    print(int(i) * 2)


rep = int(input())

for i in range(rep):
    names.append(input())

for j in names:
    a = j.split()
