class User :
        def __init__(self, id, password):
                self.userID = id
                self.__password = password

        def getID(self):
                return self.userID
        
        def checkPassword(self, password):
                if(self.__password == password):
                        return True
                return False
        
        
                