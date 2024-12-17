from entities import affiliation, serviceCharge

class unionAffiliation(affiliation):
    __dues: int
    __serviceCharge: serviceCharge

    def __init__(self, dues):
        self.__dues = dues

    def charge(self):
        pass

    def addServiceCharge(self, charge)