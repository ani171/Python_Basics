#Tkinter
#Opening tkinter page/window

from tkinter import *
root=Tk()
#Creating a label-pack() geometry manager

from tkinter import *
root=Tk()
label=Label(root,text="Hey").pack()
root.mainloop()
#grid() geometry manager

from tkinter import *
root=Tk()
label=Label(root,text="Hey").grid(row=0,column=0)
root.mainloop()
#Button operations

from tkinter import *
root=Tk()
button=Button(root,text="I am button").grid(row=1,column=30)
button1=Button(root,text="I am disabled",state=DISABLED).grid(row=0,column=0)#Creating a disabled button
button2=Button(root,text="Hi I changed my size",padx=20,pady=20).grid(row=10,column=10)#Changing dimensions
def act():
    b=Button(root,text="Thanks for clicking").grid(row=10,column=5)
button3=Button(root,text="Click here",command=act).grid(row=23,column=23)
button4=Button(root,text="Colored me",bg="black",fg="gold",font=("times",11)).grid(row=15,column=15)
button5=Button(root,text="Exit",command=root.destroy).grid(row=55,column=55)#Exit button
root.mainloop()
#Mesaage box operations

from tkinter import *
root=Tk()
e=Entry(root).pack() #Creating message box
root.mainloop()
from tkinter import *
root=Tk()            
e=Entry(root,fg="cyan",bg="black",borderwidth=5)
e.pack()
e.insert(0,"Hey ")#For default text in the message box
def action():
    
    my=Label(root,text=e.get())
    my.pack()
    
button=Button(root,command=action,text="Click here").pack()
root.mainloop()
#To apply image

from tkinter import *
from PIL import ImageTk,Image
root=Tk()
img=ImageTk.PhotoImage(Image.open(r"C:\Users\Anirudh\Desktop\123.jpg"))
label=Label(image=img).pack()
root.mainloop()
#Changing Icon of the window

from tkinter import *
root=Tk()
root.iconbitmap(r'C:\Users\Anirudh\Desktop\apple_juice_drink_fruit_icon_210166.ico')
root.mainloop()
#Operations on Canvas

from tkinter import *
root=Tk()
mycan=Canvas(root,bg="blue",height=1000,width=1000)
coord=10,20,240,200
arc=mycan.create_arc(coord,start=10,fill="black") #Creating arc
mycan.pack()
root.mainloop()

from tkinter import*
root=Tk()
c=Canvas(root,width=1000,height=1000,bg="red")
polygon=c.create_polygon(0,0,100,0,100,100,50,150,0,100,0,0,fill="green") #Creating polygon
c.pack()
root.mainloop()

from tkinter import*
root=Tk()
c=Canvas(root,width=500,height=500,bg="green")
line=c.create_line(100,200,300,400,fill="red") #Creating line
c.pack()
root.mainloop()

from tkinter import*
root=Tk()
c=Canvas(root,bg="yellow",width=500,height=500)
circle=c.create_oval(110,110,210,210,fill="red") # x0 and y0 should same, x1,y1 same; Creating oval
c.pack()
root.mainloop()

#Opeartions on frames

from tkinter import *
root=Tk()
root.geometry('1500x750')
frame=Frame(root,bg="gold",width=750,height=1500).pack(fill=BOTH)
root.mainloop()

from tkinter import *
root=Tk()
frame=Frame(root,bg="gold",width=75,height=150,relief=RAISED,borderwidth=10).pack(fill=BOTH)#Raised frame
root.mainloop()

from tkinter import *
root=Tk()
frame=Frame(root,bg="gold",width=75,height=150,relief=SUNKEN,borderwidth=10).pack(fill=BOTH) #Sunken Frame
root.mainloop()

from tkinter import *
root=Tk()
frame=Frame(root,bg="gold",width=75,height=150,relief=FLAT,borderwidth=10).pack(fill=BOTH) #Flat frame no changes
root.mainloop()

from tkinter import *
root=Tk()
frame=Frame(root,bg="gold",width=75,height=150,relief=GROOVE,borderwidth=10).pack(fill=BOTH) #Groove like frame is created
root.mainloop()

#Operations on Checkbox
from tkinter import *
root= Tk()
a=Checkbutton(root, text='male').grid(row=0)
b=Checkbutton(root, text='female').grid(row=1)
root.mainloop()
