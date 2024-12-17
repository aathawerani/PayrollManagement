from entities import employee

employeesList = list[employee]

class dataStore:
    __employeeList = employeesList

    def addEmployee(self, emp):
        self.__employeeList.append(emp)