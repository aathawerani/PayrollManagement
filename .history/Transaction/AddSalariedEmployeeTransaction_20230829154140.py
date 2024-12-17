from Transaction.AddEmployeeTransaction import addEmployeeTransaction
from entities.HourlyClassification import hourlyClassification

class addSalariedEmployeeTransaction(addEmployeeTransaction):

    def __init__(self, name, address, monthly, method, aff, schedule):
        super(name, address)
        self.setPaymentMethod(method)
        self.setAffiliation(aff)
        self.setSchedule(schedule)
        self._paymentClassification = hourlyClassification(monthly)

    def validate(self): 
        pass

    def execute(self):
        self.addToStore()

