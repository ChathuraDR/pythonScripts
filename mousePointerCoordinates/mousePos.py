import sys
import time, sys
import pyautogui

ncolr = '\x1b[0m'
colr = '\x1b[6;31m'

while True:
    crnt_pos = pyautogui.position()
    sys.stdout.write("\r" + ncolr + "[*] Mouse current X coordinates:" + colr + str(crnt_pos[0]) + ncolr + " and Y coordinates:" + colr + str(crnt_pos[1]) + ncolr)
    sys.stdout.flush()