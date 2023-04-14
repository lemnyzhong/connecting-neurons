from Faculties import Faculties
from Utils import utils

class Session:

    def __init__(self):
        self.faculties = Faculties()

    def use(self):
        # Print out the help menu
        self.helpMenu()
        choice = input("Command (L/X): ")
        while choice != 'X':
            if (choice == 'L'):
                self.login()
            else:
                self.helpMenu()

            choice = input("Command (L/X): ")
    
        print("\nSession Terminated!")

    def login(self):
        # Read in the email and password
        faculty = self.faculties.faculty(input("Email: "), input("Password: "))
        if faculty is not None:
            faculty.use()
            print("\nTMS Tuition Management System:")
        else:
            print("Incorrect faculty details!")

    def helpMenu(self):
        print("Tuition Management System:")
        print("L- Login")
        print("X- Exit")

if __name__ == "__main__":
    Session().use()

