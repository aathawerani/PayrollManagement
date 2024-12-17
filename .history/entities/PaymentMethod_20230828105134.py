from abc import ABC, abstractmethod

class paymentMethod(ABC):
    @abstractmethod
    def CalculatePay(self):
        pass
 