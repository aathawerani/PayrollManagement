from Transaction import addCommissionedEmployeetransaction

class parser():

    def parseTransaction(self, transactionType):
        
        if(transactionType == "AddCommissionedEmployee"):
            transaction = addCommissionedEmployeetransaction()