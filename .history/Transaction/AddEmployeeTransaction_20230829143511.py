from Transaction import transaction
from entities import affiliation, holdMethod, directMethod, mailMethod, paymentMethod

class addEmployeeTransaction(transaction):
    __name: str
    __address: str
    __paymentMethod: paymentMethod

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

    def getPaymentMethod(self, method):
        if(method == "Direct"):
            return directMethod()
        elif(method == "Hold"):
            return holdMethod()
        elif(method == "Mail"):
            return mailMethod
        