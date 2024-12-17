from PayClassification import payClassification
from SaleReceipt import saleReceipt

class SalariedClassification(payClassification):
    __monthlyPay: int

    def __init__(self, monthly):
        self.__monthlyPay = monthly

    def CalculatePay(self):
        pass
