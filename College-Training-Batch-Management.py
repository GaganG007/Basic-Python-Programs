import sys
class Student:
    def __init__(self, name, rollnumber, attendence):
        self.name = name
        self.rollnumber = rollnumber
        self.attendance = attendance

print("Welcome to Python Problem Solving Program")
name=input("Enter the student name: ")
rollnumber=int(input("Enter the student roll number: "))
attendance=int(input("Enter the student attendance percentage: "))
student1=Student(name, rollnumber, attendance)
if student1.attendance >=75:
    print(f"Student is Eligible")
else:
    print("Student Not Eligible")
sys.exit()
print(f"Student name:{student1.name}")
print(f"Student roll number:{student1.rollnumber}")
print(f"Student attendance percentage:{student1.attendance}")