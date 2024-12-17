from Employee import employee

employeesList = list[employee]

class dataStore:
    global employeeList
    employeeList = employeesList

    def addEmployee(self, emp):
        employeeList.append(emp)