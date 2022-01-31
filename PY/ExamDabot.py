import random

vocals = {"a", "e", "i", "o", "u"}
while True:
    var = list(input())
    for i in range(len(var)):
        if var[i] in vocals:
            var[i] = str(random.randint(1, 5))
    print("".join(var))
