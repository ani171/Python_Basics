#Value returning function

def f(x,y):  #Here x,y are called parameters
    print((x+y)/2)
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
f(n1,n2) #Values of n1 and n2 are called arguments

def  hello(name):
    print("Hello",name,"!","How are you?")
nn=input("Enter a name:")
hello(nn)

#Non value returning function- MUST CONTAIN RETURN STATEMENT
def double(x):
    return x*2
y=int(input("Enter a number:"))
print(double(y))

#Positional argument
def si(p,t,r):
    print((p*t*r)/100)
si(35000,4,0.05) #Here p by default takes 35000, t takes 4 and r takes 0.05

#Keyword argument
def si(p,t,r):
    print((p*t*r)/100)
si(t=4,p=35000,r=0.05)#Here argument is specified with parameter name

#Default argument
def si(p,r,t=2):#PRO-TIP==> IN ARGUMENTS DEFAULT ARGUMENT MUST NOT BE FOLLOWED BY NON-DEFAULT ARGUMENT
    print((p*t*r)/100)
si(p=35000,r=0.05)#Here t as a default for all cases is 2
#Countdown using functions
msg=input("Enter the message you want at the end of countdown:")
x=int(input("Enter the time required for countdown:"))
def count_down(n):
    while n>=0:
        if (n!=0):
            print(n,"......")
        else:
            print("0 \n",msg,"!!")
        n-=1
count_down(x)

#Global variable- a variable defined outside the function
m=100# m is the global variable
def f(count):
    if count<m:
        print("The number",count,"is less than 100")
    else:
        print("The number",count,"is greater than 100")
x=int(input("Enter a number:"))
print(f(x))

#Recursion-Function calling itself

#To find factorial of a number
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
x=int(input("Enter a number whose factorial  is to be found:"))
print(factorial(x))

#Sum of n terms
#Sum of n terms
def sum_(start):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

#Another example
def fact(n):
    if n==0:
        return 0
    else:
        return fact(n-1) +2
x=int(input("Enter a number whose factorial  is to be found:"))
print(fact(x))

#Number of unique grid paths
def grid(n,m):
    if n==1 or m==1:
        return 1
    else:
        return grid(n,m-1)+grid(n-1,m)

#Tower of Hanoi
def toh(n, from1, to, aux):
    if n==1:
        print("Move ring 1 from",from1,'peg', to, "peg")
        return
    toh(n-1, from1, aux, to)
    print("Move ring", n, "from",from1,"peg", to, "peg")
    toh(n-1, aux, to, from1)
num=int(input("Enter number of discs:"))
toh(num,'left','right','middle')

#Maximum element in a list
def max_(l):
    if len(l)==1:
        return l[0]
    else:
        return max(l[0],max_(l[1:]))
list_=[2,4,5,67,23,12,34]
list__=[12]
print(max_(list_),max_(list__))

#Finding the greatest common divisor
def GCD(x,y):
    r=x%y
    if(r==0):
        return y
    else:
        return GCD(y,r)
print(GCD(65,91))
    
#Callback 
def f1(x):
    return (x+1)
def f2(y):
    return (y+1)
def f3(z):
    return z+1
a=int(input("Enter a number:"))
print(f1(f2(f3(a))))

#Closure
def super(x):
    def sub():
        print(x)
    return sub
x=super("Hello")
del super
x() #Here even though the outer super function is deleted the inner sub function dosen't get deleted
#Finding nth root
def root(x):
    def num(y):
        return y**(1/x)
    return num
n=int(input("Enter the number whose root is to be found:"))
n1=int(input("Enter the root:"))
a=root(n1)
print(a(n))

#Decorator
def f(func):
    def inn(*a):
        print("inner")
        func(*a)
        print("after")
    return inn

@f
def s(x,y): 
    print(x+y)
s(1,2)

@f
def mul(x,y):
    print(x*y)
mul(3,6)

@f
def f3(x):
    print(sum(x),max(x))
f3([1,2,3])

