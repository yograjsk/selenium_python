'''
try:
    errorOccured = False
    z=10
    print(z)
    
except NameError:
    print("Name Error: Please assign value to the variable")
    errorOccured = True
except ZeroDivisionError:
    print("Zero Error: Value can not be divided by ZERO")
    errorOccured = True
    
except Exception:
    print("some other error occured")
    errorOccured = True
#finally:
if (errorOccured is True):
    print("Error has occured")
else:
    print("code is clean, no error observed")



def listOfStudents(listOfStudents=["abc","xyz"]):
    print("Below is the list of students")
    for x in listOfStudents:
        print(x)

students=["Anu","Madhavi","Yograj"]
listOfStudents()



def checkHasZero(numberList):
    hasZero = False
    for x in numberList:
        if(x is 0):
            hasZero = True
    return hasZero

print(checkHasZero([1,2,3,4,10,7]))

'''

def subtract(a,b):
    print(a-b)

subtract(b=20,a=10)




nums=[1,2,0,3,0,4,10,7,0]














