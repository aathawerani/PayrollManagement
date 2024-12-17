class employee:
    __name: str
    __address: str

    def __init__(self, name, address):
        __name = name
        __address = address

    def getName(self):
        return __name
    
    def getAddress(self):
        return __address
