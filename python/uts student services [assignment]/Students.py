from Student import Student
from Utils import utils

class Students:

    def __init__(self):
        self.students = []
        self.students.append(Student("Thomas Muller", "thomas.muller@uts.com", "99991111", "3 Byern St. Sydney 2001", "13697480", "Full-Time", 48, 4000.00, ""))
        self.students.append(Student("Alice Stefan", "alice.stefan@uts.com", "88881111", "24 Pitt St. Sydney 2001", "1451780", "Part-Time", 24,0.00, ""));
        self.students.append(Student("Lucy Lu", "lucy.lu@uts.com", "98981100", "11 Hunter St. Sydney 2100", "13267102", "Full-Time", 48, 0.00, "2022AUT"));
        self.students.append(Student("Andreas Brehme", "andreas.b@uts.com", "90001222", "91 Sussex St. Sydney 2100", "1367820", "Full-Time", 48, 0.00,""));
        self.students.append(Student("Ruddy Voller", "ruddy.v@uts.com", "98980000", "15 Stan St. Sydney 2100", "13972870", "Full-Time", 48, 8000.00,""));
        self.students.append(Student("Monica Shwarz", "monica.s@uts.com", "92241188", "155 Jones St. Sydney 2001", "13859610", "Part-Time", 24, 0.00, "2022AUT"));

    def viewStudents(self):
        utils.studentHeader()
        for student in self.students:
            print(utils.studentFormat(student.name, student.email, student.phone, student.studyType))
        utils.studentTableEnd()

    def addStudent(self):
        name, email, phone, address, idNumber, studyType, credits, scholarship, deductionCode = self.readStudentInformation()
        self.students.append(Student(name, email, phone, address, idNumber, studyType, credits, scholarship, deductionCode))
        print(name + " record has been created.")

    def viewStudent(self):
        # Find the Student
        name = input("Name: ")
        student = self.student(name)
        if student is not None:
            utils.studentHeader()
            print(utils.studentFormat(student.name, student.email, student.phone, student.studyType))
            utils.studentTableEnd()
        else:
            print(name + " record does not exist!")

    def updateStudent(self):
        # Find the student
        findName = input("Name: ")
        student = self.student(findName)
        if student is not None:
            print("Updating " + student.name + " record: ")
            student.updateStudent(input("Name: "), input("Email: "), input("Phone: "), input("Address: "), input("Type: "), int(input("Credits: ")), float(input("Scholarship($): ")), input("Deduction Code: "))
            print(student.name + " record has been updated.")
        else:
            print(findName + " record does not exist!")
        
    
    # Helper function to read in all the student information and return it.
    def readStudentInformation(self):
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        address = input("Address: ")
        idNumber = input("ID: ")
        studyType = input("Type: ")
        credits = int(input("Credits: "))
        scholarship = float(input("Scholarship($): "))
        deductionCode = input("Deduction Code: ")
        return name, email, phone, address, idNumber, studyType, credits, scholarship, deductionCode

    def deleteStudent(self, name):
        findName = name
        student = self.student(findName)
        if student is not None:
            self.students.remove(student)
            print(student.name + " record has been deleted.")
        else:
            print(findName + " record does not exist!")


    def student(self, name):
        for student in self.students:
            if student.matches(name):
                return student
        
        return None

    def getStudents(self):
        return self.students

