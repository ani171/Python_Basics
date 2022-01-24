#Creating a list
a=(1,2,3,"Hi","*")
b=list(a)
print(b)
x=[1,2,3,4,5,6,7,8,9,0]
print(x)
#Operations on list
l1=[1,2,3,4,5,6]
#Index of 1 is 0, 2 is 1,3 is 2 and so on
l1[2]=65#Replaces ==> list[index]=to be replaced value
print(l1)
del l1[2]#Deletes value at particular index
print(l1)
l1.insert(0,3)#Insertion ==>(index,value_to_be_inserted)
print(l1)
l1.append(7)#Adds value in () at last
print(l1)
l1.reverse()#Reverse of given list NOT DESCENDING ORDER
print(l1)
l1.sort()#Ascending order
print(l1)
'''Reverse of sort gives Descending order'''
#Heterogenous list can't be used for sorting ==> a.sort();print(a)==> INVALID ==>ATTRIBUTE ERROR
ax=[11,12,13,14,15,16,17,18,19,20]
print(ax[1:7:2])#[start:end:increment]=>start-inclusive;end-exclusive
                #Here output will be [12,14,16]
print(ax[::-1])#Rverse of list ax but NOT DESCENDING ORDER


