class Calculation1:
    def summation(self,a,b):
        # print(str(a+b))
        return a+b

    def Result(self,a,b):
        print("summation result is:",str(a+b))

class Calculation2:
    def multiplication(self,a,b):
        # print(str(a*b))
        return a*b

    def Result(self,a,b):
        print("multiplication result is:",str(a+b))

class Derived(Calculation2, Calculation1):
    def division(self, b, a):
        print("another division",str(b/a))
        return a / b

    def division(self,a,b):
        super().summation(a,b)
        super().multiplication(a,b)
        super().Result(a,b)
        print("first division",str(a/b))
        return a/b



# class Calculator(Calculation1, Calculation2, Derived):
#     pass

cal = Derived()
print(cal.summation(5,10))
print(cal.multiplication(5,10))
print(cal.division(100,5))


# d = Derived()
# print(d.summation(5,10))
# print(d.multiplication(5,10))
# print(d.division(100,5))
