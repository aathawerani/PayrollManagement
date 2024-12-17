from Transaction import addEmployeeTransaction
from entities import commissionedClassification

class addCommissionedEmployeeTransaction(addEmployeeTransaction):
    __basePay: int
    __commissionRate: float
    __paymentClassification = commissionedClassification()

    def __init__(self, base, commission, name, address, method, aff, schedule):
        self.__basePay = base
        self.__commissionRate = commission
        self.setPaymentMethod(method)
        super(name, address)

    def validate(self): 
        pass

    def execute(self):
        commissioned = commissionedClassification(self.__basePay, self.__commissionRate)
        emp = employee(self.getName(), self.getAddress(), self.__paymentClassification, 
                       self.getPaymentMethod(), self.getAffiliation(), self.getSchedule())
        
