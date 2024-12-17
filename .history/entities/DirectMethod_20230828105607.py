from entities import paymentMethod

class directMethod(paymentMethod):
    __bank: str
    __account: str

    def __init__(self, bank, account):
        self.__bank = bank
        self.__account = account

    def dispatch():
        pass