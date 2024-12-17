from entities import affiliation, serviceCharge

serviceChargeList = list[serviceCharge]

class unionAffiliation(affiliation):
    __dues: int
    __serviceCharge: serviceChargeList

    def __init__(self, dues):
        self.__dues = dues

    def charge(self):
        pass

    def addServiceCharge(self, charge):
        self.__serviceCharge.append(charge)
