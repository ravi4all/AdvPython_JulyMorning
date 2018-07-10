class Vehicle():

    tyres = 0
    gear = 0
    engine = True

    # this(self) - referes to current object
    def showVehicle(self):
        print("Vehicle details are : ")
        print("Tyres :",self.tyres)
        print("Gear :",self.gear)
        print("Engine :",self.engine)

car = Vehicle()
car.tyres = 4
car.gear = 5
car.showVehicle()

bike = Vehicle()
bike.tyres = 2
bike.gear = 5
bike.showVehicle()

cycle = Vehicle()
cycle.tyres = 2
cycle.gear = 4
cycle.engine = False
cycle.showVehicle()

