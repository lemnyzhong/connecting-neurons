#from Faculty import Faculty
from Students import Students
from Student import Student
from TMSLog import TMSLog
from Utils import utils
from Slip import Slip

class TMS:

    #private double totalTuition;
    #private double totalScholarship;
    #private double totalNetFee;
    #private double totalDeduction;
    #private double bas;
    #private String name;
    #private Students students;
    #private Faculty faculty;

    def __init__(self, faculty, students):
        self.faculty = faculty
        self.students = students
        self.slips = []
        self.generateSlips()

    def generateSlips(self):
        for student in self.students.getStudents():
            self.slips.append(Slip(student))

    def viewReport(self):
        print("TMS Report: ")
        utils.slipHeader()
        for slip in self.slips:
            slip.viewSlip()
        utils.slipTableEnd()
        

        # Calculate all tuitions, scholarships, net fees, deductions, bas
        tuitionTotal, scholarshipTotal, netFeeTotal, deductionTotal, basTotal = self.calculateTotals()
        print("")
        utils.totalsTableHeaderAndEnd()
        print(utils.totalsFormat("Total Tuition", tuitionTotal))
        print(utils.totalsFormat("Total Scholarship", scholarshipTotal))
        print(utils.totalsFormat("Total NetFee", netFeeTotal))
        print(utils.totalsFormat("Total Deduction", deductionTotal))
        print(utils.totalsFormat("Total Bas", basTotal))
        utils.totalsTableHeaderAndEnd()

    def calculateTotals(self):
        tuitionTotal = 0
        scholarshipTotal = 0
        netFeeTotal = 0
        deductionTotal = 0
        basTotal = 0
        for slip in self.slips:
            tuitionTotal += slip.tuition
            scholarshipTotal += slip.scholarship
            netFeeTotal += slip.net
            deductionTotal += slip.deduction
            basTotal += slip.bas

        return tuitionTotal, scholarshipTotal, netFeeTotal, deductionTotal, basTotal

    def viewSingleSlip(self):
        # Read in the name
        name = input("Name: ")
        # Find the slip
        slip = self.findSlip(name)
        # Print out the slip
        if slip is not None:
            print("Tuition Slip:")
            utils.slipHeader()
            slip.viewSlip()
            utils.slipTableEnd()
        else:
            print("Tuition slip does not exist for " + name + "!")

    def findSlip(self, name):
        for slip in self.slips:
            if slip.matches(name):
                return slip
        return None

    def setName(self, idNumber):
        self.name = self.faculty.name + str(idNumber)

    def getName(self):
        return self.name

    def archiveReport(self, tmsLog):
        tmsLog.archive(self)

    def showLog(self, tmsLog):
        tmsLog.showLog()

    def retrieveReport(self, tmsLog):
        tmsLog.retrieve(input("RecordID: "))

    def matches(self, recordId):
        return recordId == self.name

    def use(self, tmsLog):
        self.helpMenu()
        choice = input("Session Admin: " + self.faculty.name + " - Menu Commands (F/V/A/R/S/X): ")
        while choice != 'X':
            if choice == 'F':
                self.viewSingleSlip()
            elif choice == 'V':
                self.viewReport()
            elif choice == 'A':
                self.archiveReport(tmsLog)
            elif choice == 'R':
                self.retrieveReport(tmsLog)
            elif choice == 'S':
                self.showLog(tmsLog)
            else:
                self.helpMenu()

            choice = input("Session Admin: " + self.faculty.name + " - Menu Commands (F/V/A/R/S/X): ")

    def helpMenu(self):
        print("TMS Menu: ")
        print("F- Find Tuition Slip")
        print("V- View TMS Report")
        print("A- Archive TMS Report")
        print("R- Retrieve TMS Report")
        print("S- Show TMS Log")
        print("X- Close")


