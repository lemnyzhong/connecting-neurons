from Utils import utils
from Students import Students
from TMSLog import TMSLog
from TMS import TMS

class Faculty:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        self.students = Students()
        self.tmsLog = TMSLog()

    def matches(self, email, password):
        return self.email == email and self.password == password

    def use(self):
        self.helpMenu()
        choice = input("Session Admin: " + self.name + " - Menu Commands (C/R/U/D/V/T/X): ")
        while choice != 'X':
            if choice == 'C':
                self.addStudent()
            elif choice == 'R':
                self.viewStudent()
            elif choice == 'U':
                self.updateStudent()
            elif choice == 'D':
                self.deleteStudent()
            elif choice == 'V':
                self.viewStudents()
            elif choice == 'T':
                self.tmsMenu()
                print("\nFaculty Menu:")
            else:
                self.helpMenu()
            
            choice = input("Session Admin: " + self.name + " - Menu Commands (C/R/U/D/V/T/X): ")

    def viewStudents(self):
        self.students.viewStudents()

    def addStudent(self):
        self.students.addStudent()

    def viewStudent(self):
        self.students.viewStudent()

    def updateStudent(self):
        self.students.updateStudent()

    def deleteStudent(self):
        self.students.deleteStudent()

    def tmsMenu(self):
        TMS(self, self.students).use(self.tmsLog)
        
    
    def helpMenu(self):
        print("Admin Menu: ")
        print("C- Add Student")
        print("R- View Student")
        print("U- Update Student")
        print("D- Delete Student")
        print("V- View Students")
        print("T- TMS Menu")
        print("X- Logout")
