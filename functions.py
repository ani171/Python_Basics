#Value returning function
def f(x,y):
    print((x+y)/2)
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
f(n1,n2)

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

        





    


    












