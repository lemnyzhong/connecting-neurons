class pearlCard :
    def __init__(self, id, accVal, password):
        self.id = id
        self.accVal = accVal
        self.__password = password
    
    def checkPassword(self, password):
        if (password == self.__password):
            return True
        else:
            return False