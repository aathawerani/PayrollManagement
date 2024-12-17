from Employee import employee

employeesList = list[employee]

class dataStore:
    global employeeList
    employeeList = []

    def addEmployee(self, emp):
        employeeList.append(emp)