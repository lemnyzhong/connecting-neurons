# log in function
from user import *
import time

users = []

def createAcc(id, password):
    users.append(User(id, password))

def logIn(id, password) -> bool:
    for user in users:
        if(id == user.getID() and user.checkPassword(password)):
            time.sleep(3.0)
            print("\nLog in successful...\n")
            return True
        
    print("Incorrect Details!\n")
    return False

