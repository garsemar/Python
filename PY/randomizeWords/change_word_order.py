def change_word_order(word, list_nums):
    rand_word = word[0]
    for j in range(len(list_nums)):
        rand_word += word[list_nums[j]]
    if word[-1] == "," or word[-1] == ".":
        rand_word += word[-2]
    rand_word += word[-1]
    return rand_word