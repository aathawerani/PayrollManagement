from Transaction import addEmployeeTransaction
from entities import biWeeklySchedule, commissionedClassification, employee, affiliation, holdMethod

class addCommissionedEmployeeTransaction(addEmployeeTransaction):
    __basePay: int
    __commissionRate: float

    def __init__(self, base, commission, name, address, pay, method, aff, schedule):
        self.__basePay = base
        self.__commissionRate = commission
        super(name, address)

    def validate(self): 
        pass

    def execute(self):
        biweekly = biWeeklySchedule()
        commissioned = commissionedClassification(self.__basePay, self.__commissionRate)
        aff = affiliation()
        method = holdMethod()
        emp = employee(self.getName(), self.getAddress(), pay, method, aff, schedule)
        pass

