import time
import os

idMouse = os.popen("xinput list | grep Mouse | grep -oP 'id=.{3,3}' | cut -d= -f2").read().strip()
idKey = os.popen("xinput list | grep keyboard | tail -1 | grep -oP 'id=.{3,3}' | cut -d= -f2").read().strip()

os.system(f'xinput float {idMouse}')
os.system(f'xinput float {idKey}')

time.sleep(10)

num = 2
num2 = 3

commandMo = f"xinput reattach {idMouse} {num}"
commandKey = f"xinput reattach {idKey} {num2}"

os.system(commandMo)
os.system(commandKey)
