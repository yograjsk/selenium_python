class Bank:
    def getROI(self):
        return 10

class SBI(Bank):
    pass
    # def getROI(self):
    #     return 8

class ICICI(Bank):
    pass
    # def getROI(self):\
    #     return 9

b1 = Bank()
b2 = SBI()
b3 = ICICI()

print("Base Rate of Interest:", b1.getROI())
print("SBI Rate of Interest:", b2.getROI())
print("ICICI Rate of Interest:", b3.getROI())
