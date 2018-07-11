import controller

def addStudent():
    studentName = input("Enter student Name : ")
    studentCourse = input("Enter student Course : ")
    studentAge = int(input("Enter student Age : "))
    studentCgpa = int(input("Enter student CGPA : "))

    data = controller.add(studentName,studentCourse,studentAge,studentCgpa)
    print("Data Inserted Successfully...")
    for d in data:
        print(d)

def readStudent():
    s = input("Enter name of student : ")
    data = controller.read(s)

def deleteStudent():
    s_id = int(input("Enter the id of student : "))
    updatedData = controller.delete(s_id)
    print("Student Deleted Successfully...")
    print(updatedData)

def searchStudent():
    pass

def updateStudent():
    pass


while True:
    print("""
    1. Add Student
    2. Read Student
    3. Delete Student
    4. Search Student
    5. Update Student
    """)

    choice = input("Enter your choice : ")

    operations = {
        "1": addStudent,
        "2": readStudent,
        "3": deleteStudent,
        "4": searchStudent,
        "5": updateStudent
    }

    operations.get(choice)()