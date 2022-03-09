#Lambda function- An anonymous function-which takes many arguments but only one expression
#Used when the function is reqd only once
#Syntax: lambda arguments: expression

str_="hello"
print(lambda str_:str_)
#Output-<function <lambda> at 0x000001809585F370> here the lambda is not being called by the print function but simply returning the function object and the memory location where it is stored.

max_=lambda a,b: a if (a>b) else b
print(max_(3,4))

#Sorting
l=[{"name":"Ramya","Shoe size":7},{"name":"Swapna","Shoe size":8},{"name":"Akshith","Shoe size":4}]
print(sorted(l,key=lambda x:x["Shoe size"]))#Output-[{'name': 'Akshith', 'Shoe size': 4}, {'name': 'Ramya', 'Shoe size': 7}, {'name': 'Swapna', 'Shoe size': 8}]

#Lambda within user defined functions
def a(x):
    return lambda y:x+y
t=a(5)
print(t(6))

#Sorting a list with sublists
#an=[sorted(x,lambda x:x[0])for x in [[1,32,3],[25,47,19],[29,12,13],[14,7]]]
#print(an)

def a(x):
    return x**2
a=lambda x:x**3
print(a(4))#Output- 64 #####ALWAYS THE LATEST FUNCTION DEFINED IS CONSIDERED#####  

x=lambda y,z:y-z
def x(y,z):
    return y+z
print(x(3,4))#Output-7

#map() function- applies a given function to all iterables
#In map() Number of inputs= Number of Outputs
#Syntax: map(function,iter)

out=map(lambda x:x+5, [1,3,5,7])
print(out) #Map object is created <map object at 0x0000020A6BF0F160>
print(tuple(out)) #Output- (6, 8, 10, 12)

def square(n):
    return n*n
n1=(1,2,3,4)
print(list(map(square,n1)))

mul=list(map(lambda a,b:a*b,[1,2,3,4],[10,10,10,10]))
print(mul)

l=[2,3,4,5]
a=list(map(lambda x: x**2 if x>4 else None,l))
print(a) #Output-[None, None, None, 25]

g=list(map((lambda x : x if x>1 else None),range(-5,5)))
print(g) #Output- [None, None, None, None, None, None, None, 2, 3, 4]

#filter() function- creates an output list for which the function returns True
#Syntax: filter(function,iter)
#Difference between filter and map
out=filter(lambda x:x>3,[1,2,3,4,5,6])
print(tuple(out)) #Output-(4,5,6)

out=map(lambda x:x>3,[1,2,3,4,5,6])
print(tuple(out)) # Output (False, False, False, True, True, True)

l=["anirudh","gopal","Madhu","nithin"]
def f(n):
    if n.startswith("a"):
        return n
a=list(filter(f,l))
print(a) #Output-['anirudh']
a=list(map(f,l))
print(a) # Output-['anirudh', None, None, None]

l=["rt","1wers","ui","34rwe","_r"]
def f(s):
    if s[0].isdigit()==False:
        return s
a=list(filter(f,l))
print(a) #Output-['rt', 'ui', '_r']

#reduce() function- applies a given function to the iterable and returns a single value
#Syntax: reduce(function,iter)

from functools import reduce #reduce is not inbuilt function
s=reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9,10])
print(s)

def a(x,y):
    return x-y
s=reduce(a,[66,33,22,11,10,9,8,7,6,5,4])
print(s)

l=["Raja","Ram","mohan","roy"]
print(reduce(lambda x,y:x+' '+y,l))

l=["Raja","Ram","mohan","roy"]
print(reduce(lambda x,y:x+' '+y,l,"Sir")) #Output- Sir Raja Ram mohan roy

xyz=["Mary","had","a","little","lamb"]
x=reduce(lambda x,y: x if len(x)>len(y) else y,xyz)
print(x) #Output-little

#filter() within map()- filters out the True values from the iterable and supplies that as the parameters to the map function
a=list(map(lambda x:x*x,filter(lambda x: x>4,[2,3,4,5,6,7])))
print(a) #Output-[25,36,49]

#map() within filter()-Output of map will be given as input list to filter
a=tuple(filter(lambda x:x*x,map(lambda x: x>4,[2,3,4,5,6,7])))
print(a)#Output-(True, True, True)

a=tuple(filter(lambda x: x>15,map(lambda x:x*x,[2,3,4,5,6,7])))
print(a) #Output-(16, 25, 36, 49)

#map() and filter() within reduce()
r=reduce(lambda x,y:x+y,map(lambda x:x*2,filter(lambda x : x<9,[1,5,7,9,11,12])))
print(r) #Filter gives-[1,5,7] taken by map to give-[2,10,14] and reduces gives 26









