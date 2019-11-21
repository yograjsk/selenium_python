class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x = Person("PersonFN", "PersonLN")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname)


x = Student("StudentFN", "StudentLN")
x.printname()