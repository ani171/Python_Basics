#File handling
#To read file
file_name=input("Enter file name:")
input_file=open(file_name,'r')
data=input_file.readlines()
print(data)#Prints the content in the text in list format
#To append and read file
file=input("Enter file name:")
input_=open(file,'a')
input_.write('line four')
input_.close()
file_=input("Enter file name:")
inp=open(file_,'r')
aa=inp.readlines()
print(aa)
#To write and read lines- Write overwrites existing content
filex=input("Enter file name:")
input_x=open(filex,'w')
input_x.write('line four')
input_x.close()
file_x=input("Enter file name:")
inpx=open(file_x,'r')
aax=inpx.readlines()
print(aax)
#To create a file
f_name=input("Enter file name:")
i_file=open(f_name,'x')
yyy=open(f_name,'w')
yyy.write("Hey, How are you? All good?")
yyy.close()
file_n=input("Enter file name:")
i_f=open(file_n,'r')
d_=i_f.readlines()
print(d_)
#to delete a file
import os
fille=input("Enter file name:")
os.remove(fille)


