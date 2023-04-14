from Student import Student
from Utils import utils

class Slip:

    def __init__(self, student):
        self.name = student.name
        self.tuition = student.totalFee
        self.scholarship = student.scholarship
        self.net = student.netFee
        self.deduction = student.deductionAmount
        self.bas = student.bas

    def viewSlip(self):
        print(utils.slipFormat(self.name, self.tuition, self.scholarship, self.net, self.deduction))

    def matches(self, name):
        return self.name == name

