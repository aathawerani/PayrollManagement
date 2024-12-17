from Transaction import transaction
from entities import affiliation, noAffiliation, unionAffiliation, holdMethod, directMethod, mailMethod, paymentMethod, paymentSchedule, weeklySchedule, monthlySchedule, biWeeklySchedule, employee

class addEmployeeTransaction(transaction):
    __name: str
    __address: str
    __paymentMethod: paymentMethod
    __affiliation: affiliation
    __schedule: paymentSchedule
    __paymentClassification: 

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
            self.__affiliation = noAffiliation()
        elif(aff == "Union"):
            self.__affiliation = unionAffiliation()

    def getAffliation(self):
        return self.__affiliation
    
    def setSchedule(self, schedule):
        if(schedule == "Weekly"):
            self.__schedule = weeklySchedule()
        elif(schedule == "BiWeekly"):
            self.__schedule = biWeeklySchedule()
        elif(schedule == "Monthly"):
            self.__schedule = monthlySchedule()

    def getSchedule(self):
        return self.__schedule
    
    def addToStore(self):
        emp = employee(self.getName(), self.getAddress(), self.__paymentClassification, 
                self.getPaymentMethod(), self.getAffiliation(), self.getSchedule())
