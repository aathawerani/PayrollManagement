from entities import payClassification, saleReceipt

salesReceiptList = list[saleReceipt]

class CommissionedClassification(payClassification):
    __basePay: int
    __commissionRate: float

    def __init__(self, base, commission):
        self.__basePay = base
        self.__commissionRate = commission

    def CalculatePay(self):
        pass

    def addSaleReceipt(self, receipt):
        self.__saleReceipt.append(receipt)

