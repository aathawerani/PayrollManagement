from entities import employee

employeesList = list[employee]

class dataStore:
    global __employeeList = employeesList

    def addEmployee(self, emp):
        self.__employeeList.append(emp)