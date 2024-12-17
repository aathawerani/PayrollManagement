from Transaction import addEmployeeTransaction
from entities import hourlyClassification

class addHourlyEmployeeTransaction(addEmployeeTransaction):

    def __init__(self, base, commission, name, address, method, aff, schedule):
        super(name, address)
        self.__basePay = base
        self.__commissionRate = commission
        self.setPaymentMethod(method)
        self.setAffiliation(aff)
        self.setSchedule(schedule)
        self.__paymentClassification = hourlyClassification()

    def validate(self): 
        pass

    def execute(self):
        pass

