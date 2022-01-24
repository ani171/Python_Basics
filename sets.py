a=[1,2,3] #or (1,2,3) or directly {1,2,3}
b=[3,4,5,6,7]#or(3,4,5,6,7) or directly{3,4,5,6,7}
a1=set(a)
b1=set(b)
print(a1,b1)
#Operations on sets
a2={1,2,3}
b2={3,4,5,6,7}
a2.add(4)
print(a2)
print(7 in a2)#Membership operator- gives TRUE or FALSE
print(len(a2))
a2.remove(2)#Removes 2 from set a2
print(a2)
print(a2|b2)#Union- all elements in a2 and b2
print(a2&b2)#Intersection-Common elements in a2 and b2
print(a2-b2)#Difference-Elements in a2 but not b2
print(a2^b2)#Symmetric difference- Elements in a2 or b2 but not in both
print(((a2|b2)-(a2&b2))==(a2^b2))# Union- Intersection= Symmetric difference\
#Frozenset
ab=frozenset(1,2,3,4,5,"%",4,"^","()")
print(ab,type(ab))



