import os

from randomize import *


def getWordsFromFile():
    # Path de la carpeta con los archivos a canviar
    pathIn = "entrada/"
    pathOut = "sortida/"
    listLines = []
    dirs = os.listdir(pathIn)

    for i in dirs:
        inp = pathIn + i
        f = open(inp, "r")
        try:
            for line in f:
                if not line.isalnum():
                    line = line[:len(line) - 1]
                listLines.append(randomize_word(line))
        except:
            listLines = []
        sort = pathOut + i
        with open(sort, "w") as myfile:
            myfile.write("")
        for j in listLines:
            with open(sort, "a") as myfile:
                myfile.write(j + '\n')
        listLines = []


getWordsFromFile()
