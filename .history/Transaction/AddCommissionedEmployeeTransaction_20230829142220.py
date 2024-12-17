from Transaction import addEmployeeTransaction
from entities import biWeeklySchedule, CommissionedClassification

class addCommissionedEmployeeTransaction(addEmployeeTransaction):
    __name: str
    __address: str

    def __init__(self, base, commission):
        self.__basePay = base
        self.__commissionRate = commission

    def validate(self): 
        pass

    def execute(self):
        biweekly = biWeeklySchedule()
        commissioned = CommissionedClassification()
        pass

