#QUESTION
#Compse a program that accepts a date as imput and writes the day of the week that date falls on

#your prgram should accept 3 command lines arguments - m(month),d(day),y(year)

M=input("Enter month: " )
d=int(input("Enter the date: "))
y=int(input("Enter the year: "))

months= ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
days=['Sunday','Monday','Tuesday','Wednesday',"Thursday",'Friday','Saturday']
m=months.index(M)+1

#Formula for the Gregorian Calendar
y1=y-(14-m)/12
x=y1+y1/4 -y1/100 +y1/400
m1=m+12*((14-m)/12)-2
d1=(d+x+(31*m1)/12)%7

print(f"On {M} {d} of year {y} : the day was {days[int(d1)]}")




