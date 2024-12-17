from AddCommissionedEmployeeTransaction import addCommissionedEmployeeTransaction
from AddHourlyEmployeeTransaction import addHourlyEmployeeTransaction 
from AddSalariedEmployeeTransaction import addSalariedEmployeetransaction

class transactionParser():

    def parseTransaction(self, json):
        transactionType = json['transactionType']
        name = json['name']
        address = json['address']
        method = json['method']
        aff = json['affiliation']
        schedule = json['schedule']
        if(transactionType == "Commissioned"):
            base = json['base']
            commission = json['commission']
            transaction = addCommissionedEmployeeTransaction(base, commission, name, address, method, aff, schedule)
        elif(transactionType == "Hourly"):
            hourlyRate = json['hourlyRate']
            transaction = addHourlyEmployeeTransaction(name, address, hourlyRate, method, aff, schedule)
        elif(transactionType == "Salaried"):
            monthly = json['monthly']
            transaction = addSalariedEmployeetransaction(name, address, monthly, method, aff, schedule)

        transaction.validate()
        transaction.execute()

        return 'Hello World!'

        