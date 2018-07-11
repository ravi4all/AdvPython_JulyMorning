# Single Level Inheritance

class Vehicle:

    def __init__(self,color,roofType):
        self.tyres = 4
        self.engine = True
        self.gear = 6
        self.color = color
        self.roofType = roofType

    def showDetails(self):
        print("Vehicle details are : ")
        print("Tyres :", self.tyres)
        print("Gear :", self.gear)
        print("Engine :", self.engine)
        print("Color :", self.color)
        print("RoofType :", self.roofType)

class Car(Vehicle):

    def __init__(self,color,roofType):
        self.color = color
        self.roofType = roofType

        super(Car, self).__init__(self.color, self.roofType)

car_1 = Car('Red','Open')
car_1.showDetails()