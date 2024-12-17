from AddEmployeeTransaction import addEmployeeTransaction
from CommissionedClassification import commissionedClassification

class addCommissionedEmployeeTransaction(addEmployeeTransaction):

    def __init__(self, base, commission, name, address, method, aff, schedule):
        super(addCommissionedEmployeeTransaction, name, address)
        self.setPaymentMethod(method)
        self.setAffiliation(aff)
        self.setSchedule(schedule)
        self._paymentClassification = commissionedClassification(base, commission)

    def validate(self): 
        pass

    def execute(self):
        self.addToStore()

        
