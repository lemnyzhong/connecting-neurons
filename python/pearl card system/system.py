from pearlCard import *
import random
import math

# list to store all created cards
allCards = []

# initialising pearlCard with id, accVal
# adds created pearlCard to allCards list
def createCard(id, accVal, password):
    allCards.append(pearlCard(id, accVal, password))

# id randomiser (5 digit length, 90000 combs)
def createId():
    id = ""
    for i in range(5):
        id += str(random.randint(0, 9))
    return id

def initialVal():
    valIn = input("How much would you like to add (10/20/50/100): ")
    while(valIn != -1):
        match valIn:
            case '10':
                return 10.0
            
            case '20':
                return 20
            
            case '50':
                return 50
            
            case '100':
                return 100
            
            case other:
                valIn = input("Sorry! That wasn't a valid amount. How much would you like to add: ")

def addVal(id):
    for card in allCards:
        if (card.id == id):
            card.accVal += initialVal()

def isValid(id, password):
    for card in allCards:
        if (card.id == id and pearlCard.checkPassword(card, password)):
            return True
    return False
    
# prints information of entered card id
def printCardInfo(id):
    for card in allCards:
        if (card.id == id):
            print()
            print("Card ID: " + str(card.id))
            print("Your acount value is: $" + str("%.2f" % card.accVal))
