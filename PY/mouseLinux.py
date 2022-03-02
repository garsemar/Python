import time
import os

idMouse = os.popen("xinput list | grep Mouse | grep -oP 'id=.{3,3}' | cut -d= -f2").read()
idKey = os.popen("xinput list | grep keyboard | tail -1 | grep -oP 'id=.{3,3}' | cut -d= -f2").read()

os.system(f'xinput float {idMouse}')
os.system(f'xinput float {idKey}')

# time.sleep(5)
#
# commandMo = 'xinput reattach ' + idMouse + ' 2'
# commandKey = 'xinput reattach ' + idKey + ' 3'
#
# os.system(commandMo)
# os.system(commandKey)
