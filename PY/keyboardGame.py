import os
from tkinter import *
from random import randint
from time import sleep


def delete():
    ran = 40
    os.system(f'xmodmap -e "keycode {ran} = "')


def restore():
    os.system("setxkbmap -layout es")


def main():
    window = Tk()
    window.title("App")

    butt = Button(window, text="Delete random key", command=lambda: delete(), height="2", width="15")
    butt.place(relx=0.1, rely=0.5, anchor=W)

    butt = Button(window, text="Restore", command=lambda: restore(), height="2", width="15")
    butt.place(relx=0.1, rely=0.8, anchor=W)

    window.mainloop()


if __name__ == '__main__':
    main()

# while True:
#     ran = randint(1, 50)
#     os.system(f'xmodmap -e "keycode {ran} = "')
#     sleep(3)
