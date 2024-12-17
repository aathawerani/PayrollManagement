from Transaction import addCommissionedEmployeetransaction, addHourlyEmployeetransaction, addSalariedEmployeetransaction, addSaleReceipttransaction, addTimeCardtransaction


class parser():

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
            transaction = addHourlyEmployeetransaction()
        elif(transactionType == "Salaried"):
            transaction = addSalariedEmployeetransaction()
        elif(transactionType == "SaleReceipt"):
            transaction = addSaleReceipttransaction()
        elif(transactionType == "TimeCard"):
            transaction = addTimeCardtransaction()

        transaction.validate()
        transaction.execute()

        return 'Hello World!'

        