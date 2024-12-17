from entities import payClassification, TimeCard

class HourlyClassification(payClassification):
    __hourlyRate: int
    __timeCard : [] 

    def __init__(self, hourly):
        self.__hourlyRate = hourly

    def CalculatePay(self):
        pass
