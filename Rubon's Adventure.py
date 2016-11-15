import sys
import time
from Assets.Order import Part as part

def cls():
    for i in range(0, 50):
        print("\n")

option=part.Menu.Start(cls)
if option==49:
    part.Demo.Start(cls)
elif option==50:
    exit()
