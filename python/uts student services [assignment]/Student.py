class Student:

    def __init__(self, name, email, phone, address, idNumber, studyType, credits, scholarship, deductionCode):
        self.updateStudent(name, email, phone, address, studyType, credits, scholarship, deductionCode)
        self.idNumber = idNumber

    def matches(self, name):
        return self.name == name

    def updateStudent(self, name, email, phone, address, studyType, credits, scholarship, deductionCode):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.studyType = studyType
        self.credits = credits
        self.scholarship = scholarship
        self.deduction = deductionCode == "2022AUT"
        self.payPerCredit = 500
        self.deductionRate = 0.1
        self.totalFee = self.credits * self.payPerCredit
        self.deductionAmount = float(self.deduction) *  float(self.totalFee) * float(self.deductionRate)
        self.netFee =  float(self.totalFee) - self.deductionAmount -  float(self.scholarship)
        self.bas = float(self.scholarship) + self.deductionAmount
