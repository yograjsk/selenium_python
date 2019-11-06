import math

n = 4
a = (1,2)
b = (3,4)
length = len(a) if a>b else len(b)

subGroup = []

#finalList = []
reject = False
finalCount = 0

for i in range(1, n + 1):
    counter=i
    for j in range(i, n + 1):
        while(counter <= j):
            subGroup.append(counter)
            counter+=1
        else:
            reject = False
            for y in range(0, length):
                if (a[y] in subGroup and b[y] in subGroup):
                    reject = True
                    break
            finalCount = finalCount+1 if reject is False else finalCount
            subGroup.clear()
            counter=i
print(finalCount)