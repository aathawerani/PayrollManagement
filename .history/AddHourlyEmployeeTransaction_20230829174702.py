from AddEmployeeTransaction import addEmployeeTransaction
from HourlyClassification import hourlyClassification

class addHourlyEmployeeTransaction(addEmployeeTransaction):

    def __init__(self, name, address, hourlyRate, method, aff, schedule):
        super(name, address)
        self.setPaymentMethod(method)
        self.setAffiliation(aff)
        self.setSchedule(schedule)
        self._paymentClassification = hourlyClassification(hourlyRate)

    def validate(self): 
        pass

    def execute(self):
        return self.addToStore()

