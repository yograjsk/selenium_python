'''
Assignment:

'''


class newEmployee:
    increment = 1.50       # static variable

    def __init__(self, fname, lname, salary):
        self.__fname = fname        # method variables  ==> private fields by adding __ to the prefix of variable name
        self.__lname = lname
        self.__salary = salary

    def getFname(self):         # to access the private fields we are creating getter method (accessor method)
        return self.__fname

    def setFname(self, fn):     # to update the private fields values we are creating setter method (mutator method)
        self.__fname = fn

    def getlname(self):
        return self.__lname

    def setlname(self, ln):
        self.__lname = ln

    def getSalary(self):
        return self.__salary

    def setSalary(self, sal):
        self.__salary = sal

    def giveIncrement(self):
        print("salary before increment: " + str(self.getSalary()))
        # a = self.getSalary()
        self.setSalary(self.getSalary()*newEmployee.increment)
        print("salary after increment: " + str(self.getSalary()))

    def giveRaise(self):
        print("before raise: " + str(self.getSalary()))
        newSalary = self.__salary * 2
        print("after raise: " + str(newSalary))

emp1 = newEmployee("testFName1", "testLName1", 30000)
emp2 = newEmployee("testFName2", "testLName2", 50000)
emp2.giveRaise()

# print(emp1.getFname())
# print(emp1.getlname())
# print(emp1.getSalary())
# emp1.giveIncrement()
#
# # emp1.setFname("testNewFname")
# # emp1.setlname("testNewLname")
#
# print(emp2.getFname())
# print(emp2.getlname())
# print(emp2.getSalary())
# # emp2.giveIncrement()
#
# #
# # emp1.getFname()
# # emp1.getlname()
#
