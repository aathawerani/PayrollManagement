from entities import payClassification, timeCard

timeCardList = list[timeCard]

class HourlyClassification(payClassification):
    __hourlyRate: int
    __timeCard : timeCardList 

    def __init__(self, hourly):
        self.__hourlyRate = hourly

    def addTimeCard(self, TimeCard):
        self.__timeCard.append(TimeCard)

    def CalculatePay(self):
        pass
