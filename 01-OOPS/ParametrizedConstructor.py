class Vehicle():

    def __init__(self, tyre, gear, engine = True):
        self.tyre = tyre
        self.engine = engine
        self.gear = gear

    def showVehicle(self):
        print("Vehicle Details")
        print("Tyre : {}, Engine : {}, Gear : {}".format(self.tyre, self.engine, self.gear))

car = Vehicle(4,5)
car.showVehicle()

bike = Vehicle(2,5)
bike.showVehicle()

cycle = Vehicle(2,4,False)
cycle.showVehicle()