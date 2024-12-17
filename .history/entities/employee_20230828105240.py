from entities import payClassification, paymentMethod

class employee:
    __name: str
    __address: str
    __paymentClassification: payClassification
    __paymentMethod: paymentMethod

    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
