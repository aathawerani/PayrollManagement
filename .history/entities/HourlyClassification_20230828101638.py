from entities import payClassification 

class HourlyClassification(payClassification):
    __hourlyRate: int

    def __init__(self, hourly):
        self.__hourlyRate = hourly

    def CalculatePay(self):
        pass
