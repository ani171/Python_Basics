#To create tuple
a=(1,)
print(a,type(a))#here type would be tuple
b=(1)
print(b,type(b))#here type would be int
ax=[1,2,3,4,"Hi","%"]
ay=tuple(ax)
print(ay)
#Operations on tuple
az=(1,2,3,4,1,2,1,2,3,1,3,4,6,7,8,1,0,5,4,6)
print(az.count(1))
print(len(az))
print(az.index(1))#If a char is present many times for index its index where its present first time will be taken


