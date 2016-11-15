import time
from msvcrt import getch

def Start(cls):
    cls()
    print("Demo\n/-----------------------\\\n/       Rubon's        \\\n\\       Adventure       /\n\\-----------------------/\n1. Start\n2. Exit")
    while True:
        key = ord(getch())
        if key==49 or key==50:
            return key
