from entities import payClassification

class employee:
    __name: str
    __address: str
    __paymentMethod: payClassification

    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
