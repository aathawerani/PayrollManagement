from Transaction.AddCommissionedEmployeeTransaction import addCommissionedEmployeetransaction
from AddHourlyEmployeeTransaction import addHourlyEmployeetransaction 
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
            transaction = addCommissionedEmployeetransaction(base, commission, name, address, method, aff, schedule)
        elif(transactionType == "Hourly"):
            hourlyRate = json['hourlyRate']
            transaction = addHourlyEmployeetransaction(name, address, hourlyRate, method, aff, schedule)
        elif(transactionType == "Salaried"):
            monthly = json['monthly']
            transaction = addSalariedEmployeetransaction(name, address, monthly, method, aff, schedule)

        transaction.validate()
        transaction.execute()

        return 'Hello World!'

        