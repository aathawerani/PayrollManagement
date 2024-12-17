from Transaction import addEmployeeTransaction
from entities import biWeeklySchedule, commissionedClassification, employee

class addCommissionedEmployeeTransaction(addEmployeeTransaction):
    __basePay: int
    __commissionRate: float
    __paymentClassification = commissionedClassification()

    def __init__(self, base, commission, name, address, method, aff, schedule):
        self.__basePay = base
        self.__commissionRate = commission
        super(name, address)

    def validate(self): 
        pass

    def execute(self):
        biweekly = biWeeklySchedule()
        commissioned = commissionedClassification(self.__basePay, self.__commissionRate)
        emp = employee(self.getName(), self.getAddress(), self.__paymentClassification, self.getPaymentMethod(method), aff, schedule)

