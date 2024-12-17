from Transaction import addEmployeeTransaction

class addHourlyEmployeeTransaction(addEmployeeTransaction):

    def __init__(self, base, commission, name, address, method, aff, schedule):
        super(name, address)
        self.__basePay = base
        self.__commissionRate = commission
        self.setPaymentMethod(method)
        self.setAffiliation(aff)
        self.setSchedule(schedule)
        self.__paymentClassification = commissionedClassification()

    def validate(self): 
        pass

    def execute(self):
        pass

