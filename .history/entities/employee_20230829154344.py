from entities.PayClassification import payClassification
from entities.PaymentMethod import paymentMethod
from entities.Affiliation import affiliation
from entities.PaymentSchedule import paymentSchedule

class employee:
    __name: str
    __address: str
    __paymentClassification: payClassification
    __paymentMethod: paymentMethod
    __affiliation: affiliation
    __paymentSchedule: paymentSchedule

    def __init__(self, name, address, pay, method, aff, schedule):
        self.__name = name
        self.__address = address
        self.__paymentClassification = pay
        self.__paymentMethod = method
        self.__affiliation = aff
        self.__paymentSchedule = schedule

    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
