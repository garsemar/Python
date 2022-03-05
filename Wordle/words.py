wrd = open("words2.txt", "r")
f = open("words.txt", "a")
for line in wrd:
    line = line[:len(line) - 1]
    line = line.lower()
    if len(line) == 5:
        if line.isalpha():
            f.write("\n")
            f.write(line)
f.close()
