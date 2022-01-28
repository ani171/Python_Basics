a="Hello"
print(a[1],type(a))#Indexing in strings are same as list
print(a[::-1])#Reverses the string
print(len(a))
#Slicing-string_name[start,end,increment]
b="Hello World"
print(b[2:7])#NOTE-THE BLANK SPACE BETWEEN O AND W'S INDEX IS 5
c= "Hello,World!"
print(c[-5:-2])#!=-1,d=-2,l=-3,r=-4.o=-5==>OUTPUT=orl
#Upper case and Lower case
print(c.upper())
print(c.lower())
print(c.casefold())#Same as lower case
print(c.swapcase())#Upper case <==> Lower case
#Strip function-Removes blankspace in start or end
d="   Mathematics!!!     "
print(d.strip()) #Output will be "Mathematics!!!"
#Replace
print(d.replace('M','Q')) #Output will be "   Qathematics!!!     "
#Split
m="Chandu Ke Chacha Ne Chandu Ki Chachi Ko Chandni-Chowk Mein Chandni Raat Mein Chaandi Ke Chammach Se Chatni Chatai"
print(m.split(" "))#Output-['Chandu', 'Ke', 'Chacha', 'Ne', 'Chandu', 'Ki', 'Chachi', 'Ko', 'Chandni-Chowk', 'Mein', 'Chandni', 'Raat', 'Mein', 'Chaandi', 'Ke', 'Chammach', 'Se', 'Chatni', 'Chatai']
n="Hi,hello,good morning,How are you?"
print(n.split(","))#Output-['Hi', 'hello', 'good morning', 'How are you?']
#Escape character-  \(backslash)==>\"string\"
txt = "We are the so-called \"Vikings\"from the north."#So that we get "Vikings"
print(txt)#Output-We are the so-called "Vikings" from the north.
abcd='abcd'
ABCD='ABCD'
print(abcd.islower())#True if str contains all lower case char's
print(ABCD.isupper())#True if str contains all upper case char's






