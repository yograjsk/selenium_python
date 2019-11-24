from abc import abstractmethod, ABC


class Bank(ABC):
    @abstractmethod
    def getROI(self):
        pass

    def getName(self):
        return "Bank Name: PARENT BANK"

class SBI(Bank):
    # pass
    # @abstractmethod
    def getROI(self):
        return 8
        # pass
    # def getROI(self):
    #     return 8
    def getName(self):
        return "Bank Name: SBI BANK"


class ICICI(Bank):
    # pass
    # def getROI(self):
    #     return 9
    # @abstractmethod
    def getROI(self):
        return 9

    def getName(self):
        return "Bank Name: ICICI BANK"

        # pass

# b1 = Bank()
b2 = SBI()
b3 = ICICI()

# print("Base Rate of Interest:", b1.getROI())
print("SBI Rate of Interest:", b2.getROI())
print("Bank Name:", b2.getName())
print("ICICI Rate of Interest:", b3.getROI())
print("Bank Name:", b3.getName())
