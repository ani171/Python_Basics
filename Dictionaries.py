#Different ways to create a dictionary
#1
a1=(["Ramu",23],["Shamu",26],["Vittal",22])
a=dict(a1)
print(a,type(a))
#2
d={"Carrot":"40/kg","Beans":"30/kg","Radish":"45/kg"}
print(d,type(d))
#3-by merging two lists
ab=["Red","Blue","Green","White"]
xy=[1,2,3,4]
dictionary=dict(zip(ab,xy))
print(dictionary,type(dictionary))
#Operations on dictionaries
#Copy
d1=dictionary.copy()
print(d1)
#To update or add a key-value
d1["Blue"]=5
print(d1)
d1["Black"]=7
print(d1)
d1.pop("Red")#To remove-d1.pop(key)
print(d1)
d1.popitem()#Popitem removes the last inserted key-value pair
print(d1)
print(d1.setdefault("Green"))#Gives the value of the key in setdefault
print(d1.get("Green"))#Function of get is same as setdefault
print(d1.keys())#Gives a tuple of all keys in given dictionary
print(d1.values())#Gives a tuple of all values in given dictionary
print(d1.items())#Gives a tuple of the key-value pairs in given dictionary
print(d1.fromkeys("123"))#Creates a dictionary with all values same for diff. keys




