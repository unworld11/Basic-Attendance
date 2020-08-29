import csv
from stud_data import *


#Datewise Attendance

today = input("Date :: ")
Headers.append(today)

for j in range(students):
    print(Column[j][1])
    ans = input("Present/Absent  input p or a ")
    if ans.lower() == 'p':
        Column[j].append("Present")
    else:
        Column[j].append("Absent")


with open("Record.csv",'w+',newline='') as file:
    z=csv.writer(file)
    z.writerow(Headers)
    z.writerows(Column)


        

        
        
    


