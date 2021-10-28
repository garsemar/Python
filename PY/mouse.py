from ctypes import *
import time

print(cdll.shell32.IsUserAnAdmin())  # Determine whether you have administrator rights

user32 = windll.LoadLibrary("C:\\Windows\\System32\\user32.dll")
user32.BlockInput(True)  # This function requires administrator privileges True to disable
time.sleep(5)
user32.BlockInput(False)  # This function requires administrator privileges
time.sleep(5)
