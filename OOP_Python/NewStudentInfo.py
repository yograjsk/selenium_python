class NewStudentInfo:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.marks)

    def averageMarks(self):
        avg = sum(self.marks)/len(self.marks)
        print("The average marks of the student: " + self.name + " is " + str(avg))

ns1 = NewStudentInfo("Vijay", [50, 20, 30, 40, 50])
ns1.display()
ns1.averageMarks()
# print(ns1.name)
# print(ns1.marks)

ns2 = NewStudentInfo("Ajay", [10,10,10, 10, 10])
ns2.display()
ns2.averageMarks()
# print(ns2.name)
# print(ns2.marks)

ns3 = NewStudentInfo("Sujay", [30, 30, 30, 30, 30])
ns3.display()
ns3.averageMarks()
# print(ns3.name)
# print(ns3.marks)



