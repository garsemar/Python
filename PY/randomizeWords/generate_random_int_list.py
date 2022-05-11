from random import randrange


def generate_random_int_list(word):
    list_nums = []
    pos = 1
    if word[-1] == "," or word[-1] == ".":
        pos = 2
    while len(list_nums) != len(word) - (pos + 1):
        r = randrange(1, len(word) - pos)
        if r not in list_nums:
            list_nums.append(r)
    return list_nums