import os

nom_archiu = input("Nombre del archibo a compilar: ")

os.system("java -jar C:/Users/marti/Desktop/Carpetas/rubber/duckencoder.jar -i C:/Users/marti/Desktop/Carpetas/rubber/sinencodear/{} -o D:\inject.bin -l es".format(nom_archiu))