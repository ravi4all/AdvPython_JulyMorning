import controller

print("""
1. Add Student
2. Read Student
3. Delete Student
4. Search Student
5. Update Student
""")

def addStudent():
    studentName = input("Enter student Name : ")
    studentCourse = input("Enter student Course : ")
    studentAge = int(input("Enter student Age : "))
    studentCgpa = int(input("Enter student CGPA : "))

    data = controller.add(studentName,studentCourse,studentAge,studentCgpa)
    print("Data Inserted Successfully...")
    print(data)

def readStudent():
    s = input("Enter name of student : ")

    data = controller.read(s)

def deleteStudent():
    pass

def searchStudent():
    pass

def updateStudent():
    pass


choice = input("Enter your choice : ")

operations = {
    "1" : addStudent,
    "2" : controller.read,
    "3" : controller.delete,
    "4" : controller.search,
    "5" : controller.update
}

operations.get(choice)()