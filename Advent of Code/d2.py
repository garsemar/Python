x = 0
y = 0
aim = 0


def forw(pos=0):
    global x
    global y
    x += pos
    y += pos*aim


def down(pos=0):
    global aim
    aim += pos


def up(pos=0):
    global aim
    aim -= pos


with open('input.txt') as f:
    moves = f.readlines()

for i in moves:
    if i[0] == "f":
        a = i[8]
        forw(int(a))
    elif i[0] == "u":
        a = i[-2]
        up(int(a))
    elif i[0] == "d":
        a = i[-2]
        down(int(a))

print(x)
print(y)
print(x*y)
