# Single Level Inheritance

class Vehicle:

    def __init__(self,tyre,gear,color,brand):
        self.tyres = tyre
        self.engine = True
        self.gear = gear
        self.color = color
        self.brand = brand

    def showDetails(self):
        print("Vehicle details are : ")
        print("Brand :",self.brand)
        print("Tyres :", self.tyres)
        print("Gear :", self.gear)
        print("Engine :", self.engine)
        print("Color :", self.color)

class Car(Vehicle):

    def __init__(self,color,brand):
        self.gear = 6
        self.tyres = 4
        self.color = color
        self.brand = brand

        super(Car, self).__init__(self.tyres,self.gear,self.color,self.brand)

class Bike(Vehicle):

    def __init__(self,gear,color,brand):
        self.tyres = 2
        self.gear = gear
        self.color = color
        self.brand = brand

        super(Bike, self).__init__(self.tyres,self.gear,self.color,self.brand)


car_1 = Car('Red','BMW')
car_1.showDetails()

bike = Bike(4,'Black','Honda')
bike.showDetails()