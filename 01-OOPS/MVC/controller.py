import model

def add(name,course,age,cgpa):
    global s
    s = model.Student(name,course,age,cgpa)
    return s.addStudent()

def read(name):
    return model.readStudent(name)

def update():
    pass

def delete(id):
    return s.deleteStudent(id)

def search():
    pass