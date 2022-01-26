#Number of days in a month program
month=int(input("Enter the month number (1-12):"))
if month in (1,3,5,7,8,10,12):
    print("The number of days in entered month are 31!")
elif month in (4,6,9,11):
    print("The number of days in entered month are 30!")
else:
    if month==2:
        year=int(input("Enter the year:"))
        if (year%4==0) and ((not(year%100==0)) or (year%400==0)):
            print("The number of days in entered month are 29!")
        else:
            print("The number of days in entered month are 28!")
    else:
        print("Invalid entry")
            
