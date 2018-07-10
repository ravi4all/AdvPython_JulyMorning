class Emp():

    def __init__(self):
        self.name = 'Ram'
        self.age = 30
        self.company = 'TCS'

    # toString = Convert Object to readable format
    def __str__(self):
        return "Emp : "+self.name+str(self.age)+self.company

    # destructor
    def __del__(self):
        print("Object Destroyed...")
        # return "Object Destroyed..."

emp_1 = Emp()
print(emp_1)