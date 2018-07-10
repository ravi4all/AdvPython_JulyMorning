class Emp():

    def __init__(self):
        self.name = 'Ram'
        self.age = 30
        self.company = 'TCS'

    def showEmp(self):
        print("Emp : ",self.name,self.age, self.company)

    # destructor
    def __del__(self):
        print("Object Destroyed...")
        # return "Object Destroyed..."

emp_1 = Emp()
emp_1.showEmp()

emp_2 = emp_1
emp_3 = emp_2

del emp_1
print("Emp_1 Object Deleted")
emp_2.showEmp()

# emp_1.showEmp()