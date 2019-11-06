class StudentMarks:

    def __init__(self, stdname, marks):
        self.stdname = stdname
        self.marks = marks

    def agerage(self):
        avg = sum(self.marks)/len(self.marks)
        print("the average of student: ", self.stdname, " is ", avg)


std1 = StudentMarks("Jayesh", [60,90,70,80,100])
print(std1.stdname)
print(std1.marks)
std1.agerage()

std1 = StudentMarks("Ramesh", [70,80,60,60,80])
print(std1.stdname)
print(std1.marks)


