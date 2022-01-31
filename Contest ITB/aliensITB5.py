rep = int(input())
names = ["Kahlest Mow'ga", "Doran Kahlest", "B'iJik Doran"]
name = []

for i in names:
    name.append(i.split())
for i in range(len(name)):
    for j in range(len(name[i])):
        if name[i][j] == name[i+1][j+1]:
            if name[i+1][j+1] == name[i+2][j]:
                print(name[i][j])
        elif name[i][j] == name[i+2][j+1]:
            if name[i+2][j+1] == name[i+1][j]:
                print(name[i][j])
