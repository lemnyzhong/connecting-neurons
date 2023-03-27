from system import *

# introduction and first choice input
print("Welcome to the Pearl Card System.\n")
print("create - to create a card        print - enter card id to view account balance       add - add money to card       help - display options        n - exit")
choice = input("Please enter your choice: ")
print()

# loop so user can exit by entering matching choice
while (choice != "n"):
    # switch/match statement for different functions
    match choice:
        # new pearlCard obj is created and added
        # prints validation message with card id number for confirmation
        case 'create':
            # crates new card ID with 5 random ints as str
            newCardId = createId()
            
            # asks for input for how much to intialise val of card
            # tests valChoice is part of available value selection
            newCardVal = initialVal()
            print()

            # try/catch value error when user enters type non-convertable to float
            #try:
                #newCardVal = float(input("How much would you like to add: "))
            #except ValueError:
                #newCardVal = float(input("Sorry! That wasn't a valid amount. How much would you like to add: "))

            createCard(newCardId, float(newCardVal), input("Please enter a password: "))
            print()
            print("Congratulations! You have a new Pearl Card.")
            print("This is your new card's id: " + str(newCardId) + "\n")

        case 'print':
            id = input("Please enter your card id: ")
            password = input("Please enter your password: ")

            while(isValid(id, password) == False):
                print()
                print("Incorrect information!\n")
                id = input("Please enter your card id: ")
                password = input("Please enter your password: ")

            printCardInfo(id)
            print()
        
        case 'add':
            id = input("Please enter your card id: ")
            password = input("Please enter your password: ")

            while(isValid(id, password) == False):
                print()
                print("Incorrect information!\n")
                id = input("Please enter your card id: ")
                password = input("Please enter your password: ")

            addVal(id)

            printCardInfo(id)
            print()

        case 'help':
            print("create - to create a card        print - enter card id to view account balance       add - add money to card       help - display options        n - exit")

        case other:
            print("Invalid Choice\n")

    choice = input("Please enter your choice: ")
    print()

print("\nThank you for using our Pearl Card System.")
print("Have a great day!\n")



