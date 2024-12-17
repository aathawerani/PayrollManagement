from abc import ABC, abstractmethod

class paymentSchedule:
    
    @abstractmethod
    def isPayDay(self, date):
        pass