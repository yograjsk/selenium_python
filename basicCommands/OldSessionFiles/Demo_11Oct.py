'''
import re

t="it was the was best wis of times wbs"
pattern1=re.compile("w.s")
matcher1=pattern1.findall(t)#it will find all the matched string and will return list

for i in matcher1:
    print(i,end=" ")


import re

pattern=re.compile("(\d\d)-(\d\d)-(\d\d\d\d)")
matcher=pattern.search("12-03-1998")

list=matcher.groups(default=None)

print("Day : ",list[0])
print("Month : ",list[1])
print("Year : ",list[2])

for - till completion of some collection, range, or set of data
while - will continue till certain condition is true
'''

list=[0,1,2,3,4,5,6,7,8]
for x in list:
    while(x < 5):
    print(x)

