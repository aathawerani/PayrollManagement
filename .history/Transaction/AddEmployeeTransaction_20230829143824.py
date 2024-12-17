from Transaction import transaction
from entities import affiliation, noAffiliation, unionAffiliation, holdMethod, directMethod, mailMethod, paymentMethod

class addEmployeeTransaction(transaction):
    __name: str
    __address: str
    __paymentMethod: paymentMethod
    __affiliation: affiliation

    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address

    def validate(self): 
        pass

    def execute(self):
        pass

    def setPaymentMethod(self, method):
        if(method == "Direct"):
            self.__paymentMethod = directMethod()
        elif(method == "Hold"):
            self.__paymentMethod = holdMethod()
        elif(method == "Mail"):
            self.__paymentMethod = mailMethod
        
    def getPaymentMethod(self):
        return self.__paymentMethod
    
    def setAffiliation(self, aff):
        if(aff == "No"):
            self.__affiliation = noAffliation()