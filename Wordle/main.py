import os
from random import *


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Wordle:
    menu = [["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"]]
    currLine = 0


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def randomWord():
    list = []
    wrd = open("words.txt", "r")
    for line in wrd:
        line = line[:len(line) - 1]
        line = line.lower()
        list.append(line)
    return list[randrange(0, len(list))]


def checkInput(secWord):
    check = 0
    val = False
    word = input("Enter a word: ")
    while True:
        wrd = open("words.txt", "r")
        for line in wrd:
            line = line[:len(line) - 1]
            line = line.lower()
            if line == word:
                val = True
                break
            else:
                val = False
        if not val:
            print("The word does not exist!")
            word = input("Enter a word: ")
        elif val:
            break
        wrd.close()
    cls()
    word = word.lower()
    addMenu(word)
    curr = Wordle.menu[Wordle.currLine]
    for i in range(len(curr)):
        if curr[i] in secWord:
            if curr[i] == secWord[i]:
                Wordle.menu[Wordle.currLine][i] = bcolors.OKGREEN + curr[i] + bcolors.ENDC
                check += 1
            else:
                Wordle.menu[Wordle.currLine][i] = bcolors.WARNING + curr[i] + bcolors.ENDC
    if check == 5:
        showMenu()
        print("You win!")
        return
    Wordle.currLine += 1
    main()

    # for i in range(len(word)):
    #     if word[i] in secWord:
    #         if word[i] == secWord[i]:
    #             color = "green"
    #             addMenu(word, i, color)
    #         else:
    #             print(bcolors.WARNING + word[i] + bcolors.ENDC + word[1:])


def addMenu(word):
    for i in range(len(word)):
        Wordle.menu[Wordle.currLine][i] = word[i]


def showMenu():
    for i in range(len(Wordle.menu)):
        for j in range(len(Wordle.menu[i])):
            print(Wordle.menu[i][j], end=" ")
        print("")


def main():
    showMenu()
    if Wordle.currLine == 6:
        print("You lose, you have exceeded the maximum attempts.")
        return
    checkInput(secWord)


if __name__ == '__main__':
    secWord = randomWord()
    print(secWord)
    print("Worlde TUI")
    print("----------")
    main()
