

list=[10,1,2,3,4,5,6,7,8,9]
print(len(list))
sum=0
for x in list:
    sum+=x
print("sum is: " + str(sum))
print("average is: " + str(sum/len(list)))

'''
dict1={'zero':0,'one':1,'two':2,'new':['zero','one',[1.0,2.0],'two',{"repeat":{'zero':0,'one':1,'two':2,'three':3,'four':4}},'four'],'five':5,'six':6}
print(dict1['new'][4]["repeat"]['four'])
'''

'''
i = 1
while i < 8:
    print(i)
    i += 1
else:
    print("i is greater than 7: "+str(i))
'''
'''
a = 20
b = 10
if b > a:
    print("b is greater than a")

if b == a:
    print("b and a are equal")

if b < a:
    print("b is lesser than a")


a = 30
b = 30
if b > a:
    print("b is greater than a")
elif b < a:
    print("b is lesser than a")
else:
    print("both a and b are equal")
'''
'''
list=[1,'two',3,"four",5.0,6,7,8]
print(list[2])
print(list[4])

list1=[1,2,3,[1,['a','b','c'],3],7,8,9]
list2=[1,2,3,(1,['a','b','c'],3),7,8,9]
print(list)
print(list1)
print(list2)
'''
'''
list1=[1,2,3,[1,('a','b','c'),3],7,8,9]
print(list1)

for x in list1:
    print(x)

print(list1[3][1][2])
'''
'''
set = {1,2,3}
print(set)

tuple=(1,'two',3,"four",5.0,6,7,8)
tuple1=(1,2,3,[1,2,3,],7,8,9)
tuple2=(1,2,3,[1,{'x','y','z'},3,],7,8,9)
print(tuple)
print(tuple1)
print(tuple2)
print(tuple2[3][1])
print(tuple2[4])
print(tuple2[5])
print(tuple2[6])
'''
'''
newlist=[0,1,2,3,4,5]
for i in newlist:
    if(i is 3):
        print("found 3")
    else:
        print("3 not found yet")
'''

'''
newtuple=(0,1,2,3,[1,{'a':0,'x':1,'y':2,'z':3},3,],7,{'a':0,'x':1,'y':2,'z':3},9)
print(newtuple[4][1]['y'])

dict1={'zero':0,'one':1,'two':2,'three':3,'four':4,'new':['zero','one',[1.0,2.0,3.0,4.0],'two','three','four'],'five':5,'six':6}
print(dict1['new'][2][1])
'''











