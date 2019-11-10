

list=[1,2,3,4,5]
for x in list1:
    print(x)


print(list[2:5])
dict={0:'zero',1:'one',2:'two',3:'three',4:'four','repeat':{0:'zero',1:'one',2:'two',3:'three',4:'four'}}
print(dict['repeat'])
newlist=["11",'22',33,44,{0:'zero',1:'one',2:'two',3:'three',4:'four','repeat':{0:'zero',1:'one',2:'two',3:'three',4:'four'}}]

list1=[0,1,2,3,4,['zero','one',[0.0,1.0,2.0,3.0,4.0],'two','three','four'],'five','six']
list2=['zero','one',2,3,4,[0,1,[1.0,2.0,3.0,4.0],'two','three','four'],5,6]
list3=[0,1,2,3,4,['zero','one',{"one":1.0,"two":2.0,"three":3.0},'two','three','four'],'five','six']
list4=[0,1,2,3,4,('zero','one',[1.0,2.0,3.0,4.0],'two','three','four'),'five','six']

for x in list1:
    print(x)
print('list '+str(list1[5][2][2]))

tuple1=[0,1,2,3,4,['zero','one',[1.0,2.0,3.0,4.0],'two','three','four'],'five','six']
tuple2=['zero','one',2,3,4,[0,1,[0.0,1.0,2.0,3.0,4.0],'two','three','four'],5,6]
tuple3=[0,1,2,3,4,['zero','one',{"one":1.0,"two":2.0,"three":3.0},'two','three','four'],'five','six']
tuple4=[0,1,2,3,4,('zero','one',[1.0,2.0,3.0,4.0],'two','three','four'),'five','six']
print('tuple '+str(tuple1[5][2][2]))

dict1={'zero':0,'one':1,'two':2,'three':3,'four':4,'new':['zero','one',[1.0,2.0,3.0,4.0],'two','three','four'],'five','six'}
dict2={'zero','one',2,3,4,[0,1,[0.0,1.0,2.0,3.0,4.0],'two','three','four'],5,6}
dict3={0,1,2,3,4,['zero','one',{"one":1.0,"two":2.0,"three":3.0},'two','three','four'],'five','six'}
dict4={0,1,2,3,4,('zero','one',[1.0,2.0,3.0,4.0],'two','three','four'),'five','six'}
print('dict '+str(dict1[new][2][2]))


#print(int('1'))
