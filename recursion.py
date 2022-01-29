#Recursion
#To find factorial of a number
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
x=int(input("Enter a number whose factorial  is to be found:"))
print(factorial(x))
#Another example
def fact(n):
    if n==0:
        return 0
    else:
        return fact(n-1) +2
x=int(input("Enter a number whose factorial  is to be found:"))
print(fact(x))
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

