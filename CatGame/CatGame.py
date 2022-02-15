master = "L"
match = ['E', master, 'S', 'I', 'R', 'T', 'M']
isV = True
out = []

f = open("cat2.dic", "r")
for line in f:
    line = line[:len(line) - 1]
    line = line.upper()
    if master in line:
        for s in line:
            if s not in match:
                isV = False
                break
            if s in match:
                isV = True
        if isV:
            print(f"{line} is valid")
            out.append(line)
        elif isV == False:
            print(f"{line} no valid")

print(out)
