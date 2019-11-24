from abc import abstractmethod, ABC



class calculator(ABC):
    @abstractmethod
    def add(self):
    # def add(self, a, b):
    # def add(self):
        pass

    @abstractmethod
    # def multiply(self, a, b):
    def multiply(self):
        pass

# abstract class: the class which has at least one abstract method

class stringCalculator(calculator):
    def add(self,a,b):
        print(str(a)+str(b))

    def multiply(self, a, b):
        print(str(a)*b)

class numberCalculator(calculator):
    def add(self, a, b, c):
        print(a + b + c)

    def multiply(self, a, b):
        print(a * b)


sc = stringCalculator()
sc.add(2,4)
# sc.multiply("abc ",2)

nc = numberCalculator()
nc.add(2,4,6)
# nc.multiply(2,4)