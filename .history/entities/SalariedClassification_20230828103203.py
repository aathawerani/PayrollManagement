from entities import payClassification, saleReceipt

saleReceiptList = list[saleReceipt]

class SalariedClassification(payClassification):
    __monthlyPay: int
    __saleReceiptList: saleReceiptList

    def __init__(self, monthly):
        self.__monthlyPay = monthly

    def addSaleReceipt(self, receipt):
        self.__saleReceiptList.append(receipt)

    def CalculatePay(self):
        pass
