"""
David Baghdasaryan
Yi Luen
ASIXcA
11/05/2022
R3: PT1_paraulesBoges
"""

import os
import pathlib
from randomize_word import *


def getWordsFromFile():
    # Path de la carpeta con los archivos
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
        with open(str(pathlib.Path(sort).with_suffix('')) + ' Boges.txt', "w", encoding='utf-8') as myfile:
            myfile.write("")
        for j in listLines:
            with open(str(pathlib.Path(sort).with_suffix('')) + ' Boges.txt', "a", encoding='utf-8') as myfile:
                myfile.write(j + '\n')
        listLines = []


getWordsFromFile()
