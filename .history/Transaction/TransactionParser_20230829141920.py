from Transaction import addCommissionedEmployeetransaction, addHourlyEmployeetransaction, addSalariedEmployeetransaction, addSaleReceipttransaction, addTimeCardtransaction

class parser():

    def parseTransaction(self, transactionType):
        
        if(transactionType == "AddCommissionedEmployee"):
            transaction = addCommissionedEmployeetransaction()
        elif(transactionType == "AddHourlyEmployee"):
            transaction = addHourlyEmployeetransaction()
        elif(transactionType == "AddSalariedEmployee"):
            transaction = addSalariedEmployeetransaction()
        elif(transactionType == "AddSaleReceipt"):
            transaction = addSaleReceipttransaction()
        elif(transactionType == "AddTimeCard"):
            transaction = addTimeCardtransaction()

        transaction.validate()
        transaction.execute()
        