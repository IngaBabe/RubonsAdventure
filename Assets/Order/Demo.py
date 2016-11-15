from msvcrt import getch
import sys
import time

class Dev():
    class Inga():
        name="Dev. Inga"
        mhp=300 ## Max HP
        hp=300 ## HP
        mmp=50 ## Max MP
        mp=50 ## MP
        attack=40 ## Physical Attack Power
        mattack=5 ## Magic Attack Power
        defence=50 ## Physical Defence
        mdefence=1 ## Magic Defence
        speed=20 ## Speed
        pguard=False ## Physical Guard
        mguard=False ## Magical Guard
    class Mushi():
        name="Dev. Mushi"
        mhp=150
        hp=150
        mmp=200
        mp=200
        attack=5
        mattack=40
        defence=1
        mdefence=50
        speed=30
        pguard=False
        mguard=False

class User():
    name=None
    mhp=250
    hp=250
    mmp=200
    mp=200
    attack=60
    mattack=50
    defence=50
    mdefence=30
    speed=25
    pmoves=["Slap", "Punch", "Clobber"]
    pdmg=[30, 50, 70]
    pguard=False
    mguard=False


def Def(u, o, cls):
    cls()
    BS(u, o)
    print("1. Physical\n2. Magical")
    while True:
        if kp(49):
            cls()
            BS(u, o)
            pguard=True
            break
        elif kp(50):
            cls()
            BS(u, o)
            mguard=True
            break

def Atk(u, o, cls):
    cls()
    BS(u, o)
    print("1. Physical\n2. Magical")
    while True:
        if kp(49):
            num=len(u.pmoves)-1
            cls()
            BS(u, o)
            for x in range(0, num):
                print(str(x+1)+" - "+u.pmoves[x]+" --", u.pdmg[x])
            for x in range(0, num):
                if rkp(x+1):
                    o.hp=o.hp-(u.attack/(o.defence^2/50))
                    break

def inifight(u, o, cls):
    while True:
        cls()
        BS(u, o)
        print("1. Attack\n2.Defend")
        u.pguard=False
        u.mguard=False
        if kp(49):
            Atk(u, o, cls)
            break
        elif kp(50):
            Def(u, o, cls)
            break

def fight(u, o, cls):
    while u.hp > 0 and o.hp > 0:
        if u.speed>o.speed:
            inifight(u, o, cls)
            ai(u, o)
        else:
            ai(u, o)
            inifight(u, o, cls)
                

def BS(u, o):
    print("                               -- "+o.name+" - "+str(o.hp)+"/"+str(o.mhp))
    print("   "+u.name+" - "+str(u.hp)+"/"+str(u.mhp)+" --")
    print("\n\n\n")

def kp(k):
    key=ord(getch())
    if key==k:
        return True

def rkp(k):
    key=getch()
    if key[len("b'"):]==str(k)+"'":
        return True

def Start(cls):
    cls()
    print("Welcome to the demo version of Rubons Adventure.\n Enter to continue.")
    while True:
        if kp(13):
            break
    while True:
        cls()
        n=input("What is your name (Enter to submit)? ")
        if n.strip(" ")!="":
            User.name=n
            break
    cls()
    print(".")
    time.sleep(.5)
    cls()
    print("..")
    time.sleep(.5)
    cls()
    print("...")
    time.sleep(2)
    cls()
    print("Dev. Inga spawned, and is ready to engage in battle!")
    time.sleep(1)
    cls()
    fight(User, Dev.Inga, cls)

    
    
