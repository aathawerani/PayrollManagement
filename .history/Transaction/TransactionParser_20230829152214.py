from Transaction import addCommissionedEmployeetransaction, addHourlyEmployeetransaction, addSalariedEmployeetransaction, addSaleReceipttransaction, addTimeCardtransaction


class parser():

    def parseTransaction(self, json):
        transactionType = json['transactionType']
        if(transactionType == "Commissioned"):
            transaction = addCommissionedEmployeetransaction()
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

        