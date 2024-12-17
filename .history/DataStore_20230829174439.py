from Employee import employee

class dataStore:
    global employeeList
    employeeList = []

    def addEmployee(self, emp):
        employeeList.append(emp)

    def getEmployeeCount(self):
        return employeeList.count