#from TMS import TMS
from Utils import utils

class TMSLog:

    def __init__(self):
        self.tmsList = []

    def archive(self, tms):
        self.tmsList.append(tms)
        tms.setName(len(self.tmsList))
        print("TMS record is created as:" + tms.getName())

    def showLog(self):
        print("TMS Archive:")
        utils.logHeader()
        for i in range(len(self.tmsList)):
            print(utils.logFormat("TMS " + str(i+1), self.tmsList[i].getName()))
        utils.logTableEnd()

    def retrieve(self, recordId):
        tms = self.tms(recordId)
        if tms is not None:
            tms.viewReport()
        else:
            print("No TMS is recorded as: " + recordId)

    def tms(self, recordId):
        for tms in self.tmsList:
            if tms.matches(recordId):
                return tms
        return None
        
        
