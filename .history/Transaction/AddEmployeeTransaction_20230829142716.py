from Transaction import transaction

class addEmployeeTransaction(transaction):
    __name: str
    __address: str

    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def validate(self): 
        pass

    def execute(self):
        pass

