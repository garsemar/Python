import ctypes
import sys
from time import sleep
from ctypes import *


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Code of your program here
    windll.user32.BlockInput(True)
    sleep(10)
    windll.user32.BlockInput(False)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
