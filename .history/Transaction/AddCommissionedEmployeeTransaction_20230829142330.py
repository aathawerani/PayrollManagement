from Transaction import addEmployeeTransaction
from entities import biWeeklySchedule, commissionedClassification, employee

class addCommissionedEmployeeTransaction(addEmployeeTransaction):
    __basePay: int
    __commissionRate: float

    def __init__(self, base, commission):
        self.__basePay = base
        self.__commissionRate = commission

    def validate(self): 
        pass

    def execute(self):
        biweekly = biWeeklySchedule()
        commissioned = commissionedClassification(self.__basePay, self.__commissionRate)
        emp = employee
        pass

