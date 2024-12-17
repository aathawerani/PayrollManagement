from entities import paymentMethod

class mailMethod(paymentMethod):
    __address: str

    def __init__(self, address):
        self.__address = address

    def dispatch(self):
        pass