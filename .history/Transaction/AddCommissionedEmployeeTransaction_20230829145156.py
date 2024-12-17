from Transaction import addEmployeeTransaction
from entities import commissionedClassification

class addCommissionedEmployeeTransaction(addEmployeeTransaction):

    def __init__(self, base, commission, name, address, method, aff, schedule):
        super(name, address)
        self.setPaymentMethod(method)
        self.setAffiliation(aff)
        self.setSchedule(schedule)
        self.__paymentClassification = commissionedClassification(base, commission)

    def validate(self): 
        pass

    def execute(self):
        self.addToStore()

        
