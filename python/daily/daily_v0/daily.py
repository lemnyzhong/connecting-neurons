import time
import os

def start_title():
    print()
    print()
    print()
    print()
    print("         Welcome to daily.          ")
    print()
    print()
    print()
    print()

def start_title2():
    print()
    print()
    print()
    print()
    print("         Welcome to daily..          ")
    print()
    print()
    print()
    print()

def start_title3():
    print()
    print()
    print()
    print()
    print("         Welcome to daily...          ")
    print()
    print()
    print()
    print()

def title_cycle():
    count = 0
    while count != 5:
        start_title()
        time.sleep(0.5)
        os.system('cls||clear')
        start_title2()
        time.sleep(0.5)
        os.system('cls||clear')
        start_title3()
        time.sleep(0.5)
        os.system('cls||clear')
        count += 1