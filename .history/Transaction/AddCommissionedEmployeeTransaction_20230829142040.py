from Transaction import addEmployeeTransaction
from entities import biWeeklySchedule

class addCommissionedEmployeeTransaction(addEmployeeTransaction):
    __name: str
    __address: str

    def validate(self): 
        pass

    def execute(self):
        biweekly = biWeeklySchedule()
        
        pass

