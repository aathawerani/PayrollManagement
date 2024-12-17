from abc import ABC, abstractmethod

class paymentMethod(ABC):
    @abstractmethod
    def charge(self):
        pass
 