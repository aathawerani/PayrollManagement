from entities import payClassification, TimeCard

timeCardArray = [TimeCard]

class HourlyClassification(payClassification):
    __hourlyRate: int
    __timeCard : timeCardArray 

    def __init__(self, hourly):
        self.__hourlyRate = hourly

    def CalculatePay(self):
        pass
