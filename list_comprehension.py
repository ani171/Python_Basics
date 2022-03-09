#List comprehension- creating new lists from other iterables
#Syntax: newlist=[expression(element) for element in old iter if condition]

r=[i**2 for i in range(6)]
print(r) #Output-[0, 1, 4, 9, 16, 25]

dou=(lambda a:a*2)
double=[dou(a) for a in range(6)]
print(double) #Output-[0, 2, 4, 6, 8, 10]

def double(a):
    if a%2==0: #acts like a map()
        r=a**2
        return r
res=[double(a) for a in range(10) ]
print(res) #Output-[0, None, 4, None, 16, None, 36, None, 64, None]

res=[y for y in range(10) if y%2==0 or  y%3==0]
print(res) #Output-[0, 2, 3, 4, 6, 8, 9]

#Even and Odd numbers
a=[("even",i) if i%2==0 else ("odd",i) for i in range(30)]
print(a)

#Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix) #Output-[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

#Tables of 10 using lambda
numbers = list(map(lambda i: i*10, [i for i in range(1,11)]))
print(numbers)

#Reversing elements in tuple
List = [string[::-1] for string in ("hello","42","$ghj")]
print(List) #Output-['olleh', '24', 'jhg$']

#Sum of individual elements
def digitSum(n):
    sum_= 0
    for i in str(n):
        sum_=sum_+ int(i)
    return sum_
List = [367, 111, 562, 945, 6726, 873]
newList = [digitSum(i) for i in List]
print(newList) #Output-[16, 3, 13, 18, 21, 18]
