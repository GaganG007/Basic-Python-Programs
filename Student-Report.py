import sys
class Student:
    def __init__(self, name, rollnumber, marks):
        self.name = name
        self.rollnumber = rollnumber
        self.marks = marks

name=input("Enter the student's name: ")
rollnumber=input("Enter the student's roll number: ")
marks=int(input("Enter the student's marks: "))
student1=Student(name, rollnumber, marks)
key=int(input("Enter the key to search (1 for Details of student, 0 to exit): "))
if key==1:
    print(f"{student1.name} with {student1.rollnumber} got {student1.marks}")
else:
    print("Byee")
    sys.exit()