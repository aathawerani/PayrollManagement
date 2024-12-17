from entities.PayClassification import payClassification
from entities.TimeCard import timeCard

timeCardList = list[timeCard]

class hourlyClassification(payClassification):
    __hourlyRate: int
    __timeCard : timeCardList 

    def __init__(self, hourly):
        self.__hourlyRate = hourly

    def addTimeCard(self, card):
        self.__timeCard.append(card)

    def CalculatePay(self):
        pass
