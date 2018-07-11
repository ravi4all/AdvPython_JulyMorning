class Student():

    __students = []
    __id = 0

    def __init__(self,name,course,age,cgpa):
        self.name = name
        self.course = course
        self.age = age
        self.cgpa = cgpa

    def __str__(self):
        return self.name + " " + self.course + " " + str(self.age) + " " + str(self.cgpa)

    def addStudent(self):
        Student.__id += 1
        Student.__students.append([self.__id, self.name, self.course, self.age, self.cgpa])
        return Student.__students

    def deleteStudent(self, id):
        for i in range(len(Student.__students)):
            if Student.__students[i][0] == id:
                print("Inside If")
                del Student.__students[i]

        return Student.__students

    def updateStudent(self):
        pass