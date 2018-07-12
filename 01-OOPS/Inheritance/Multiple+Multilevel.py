class Honda:
    def __init__(self):
        self.selfStart = True
        self.selfDriven = True
        self.powerSteering = True

class Maruti:

    def __init__(self,carName, tyreBrand, hybrid, automatic, average):
        self.carName = carName
        self.tyreBrand = tyreBrand
        self.hybrid = hybrid
        self.automatic = automatic
        self.average = average
        self.roofType = 'open'

    def showDetails(self):
        print("Hybrid : {}".format(self.hybrid))
        print("Automatic : {}".format(self.automatic))

class Swift(Maruti):

    def __init__(self, hybrid, automatic, average):
        self.carName = 'Swift'
        self.tyreBrand = 'MRF'
        self.hybrid = hybrid
        self.automatic = automatic
        self.average = average

        super(Swift, self).__init__(self.carName, self.tyreBrand, self.hybrid, self.automatic, self.average)

    # function overriding
    def showDetails(self):
        print("Details of {}".format(self.carName))
        print("Tyre Brand : {}".format(self.tyreBrand))
        print("Average : {}".format(self.average))


# obj = Swift(False, False, 20)
# obj.swiftFeatures()
# obj.showDetails()

class SwiftVersion2(Swift):

    def __init__(self,automatic,hybrid,average):
        self.automatic = automatic
        self.hybrid= hybrid
        self.average = average
        super().__init__(self.hybrid,self.automatic,self.average)

    def newFeatures(self):
        print("New features of {}".format(self.carName))
        print("Swift uses {}".format(self.tyreBrand))
        print("Average : {}".format(self.average))
        print("Automatic : {}".format(self.automatic))
        print("Hybrid : {}".format(self.hybrid))
        print("Roof Type : {}".format(self.roofType))

# obj = SwiftVersion2(True,True,15)
# obj.newFeatures()

class SwiftVersion3(SwiftVersion2,Honda):

    def __init__(self, automatic, hybrid, average):
        self.automatic = automatic
        self.hybrid = hybrid
        self.average = average
        super(SwiftVersion3, self).__init__(self.hybrid,self.automatic,self.average)
        # super(SwiftVersion3, self).__init__()

    def latestFeatures(self):
        print("New features of {}".format(self.carName))
        print("Swift uses {}".format(self.tyreBrand))
        print("Average : {}".format(self.average))
        print("Automatic : {}".format(self.automatic))
        print("Hybrid : {}".format(self.hybrid))
        print("Roof Type : {}".format(self.roofType))
        print("Self Start : {}".format(Honda.selfStart))
        print("Self Drive : {}".format(Honda.selfDriven))
        print("Power Steering : {}".format(Honda.powerSteering))

obj = SwiftVersion3(True, True, 20)
obj.latestFeatures()