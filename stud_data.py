#Attendance for Zoom

print("Attendance Register")

Headers = ['Roll No.','Name']

Column = []
students = int(input("Number of Students in class :::  "))
for i in range(students):
    roll=int(input("Enter Roll No. : "))
    name=input("Enter Name :: ")
    l=[roll,name]
    Column.append(l)

print(Column)
