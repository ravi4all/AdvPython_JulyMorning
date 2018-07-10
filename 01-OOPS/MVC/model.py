class Student():

    def __init__(self, id,name,course,age,cgpa):
        self.id = 0
        self.name = name
        self.course = course
        self.age = age
        self.cgpa = cgpa

    def __str__(self):
        return self.name + " " + self.course + " " + str(self.age) + " " + str(self.cgpa)

students = []

def addStudent(name,course,age,cgpa):
    obj = Student(id,name,course,age,cgpa)
    students.append(obj)
    return obj

def readStudent(name):
    pass
